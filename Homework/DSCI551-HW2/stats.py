from lxml import etree
import sys
import json

def dfs(id, depth):
    #print(id, depth)
    global maxDepth
    maxDepth = max(maxDepth, depth)
    for item in result:
        idt = item.xpath("./parent/text()")
        #print(idt[0], "  !@#!@")
        if idt[0] == id:
            children = item.xpath("./child/text()")
            if children != []:
                #print(children)
                for child in children:
                    #print(type(child))
                    #print(child)
                    dfs(child, depth + 1)

def findDirnFile(tree):
    numDir = 0
    numFile = 0
    global minSizeFile
    global maxSizeFile
    INodeFiles = tree.xpath("//inode")
    for item in INodeFiles:
        typeNode = item.xpath("./type/text()")
        if typeNode[0] == "DIRECTORY":
            numDir += 1
        elif typeNode[0] == "FILE":
            sizeFile = item.xpath("./blocks/block/numBytes/text()")
            if sizeFile != []:
                minSizeFile = min(minSizeFile, int(sizeFile[0]))
                maxSizeFile = max(maxSizeFile, int(sizeFile[0]))
            #print(sizeFile)
            numFile += 1
    return numDir, numFile

if __name__ == '__main__':
    maxDepth = 1
    rexml = sys.argv[1]
    outputFile = sys.argv[2]

    tree = etree.parse(rexml)
    INodeDir = tree.xpath("//INodeDirectorySection")
    #print(INodeDir)
    if INodeDir != []:
        result = tree.xpath("//directory")
        for item in result:
            id = item.xpath("./parent/text()")
            dfs(id[0], 1)
    else:
        maxDepth = 0
    print(maxDepth)
    exit()
    minSizeFile = 100000000
    maxSizeFile = -1
    numDir, numFile = findDirnFile(tree)
    print(numDir, numFile)
    if numFile == 0:
        existFile = False
    else:
        existFile = True
    print(minSizeFile, maxSizeFile)
    output = {}
    output["number of files"] = numFile
    output["number of directories"] = numDir
    output["maximum depth of directory tree"] = maxDepth
    if existFile == True:
        temp = {}
        temp["max"] = maxSizeFile
        temp["min"] = minSizeFile
        output["file size"] = temp

    with open(outputFile, 'w') as file:
        json.dump(output, file)
    print(output)


