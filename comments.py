def blank_checker(filename):
        """line is a string, returns nothing if"""
        f = open(filename,'r+').readlines()
        no_newlines = []
        for line in f:
                index = f.index(line)
                if line != '\n':
                        no_newlines.append(line)
        return no_newlines


def comment_checker(filename):
        """line is string, returns all"""

        f = open(filename,'r+').readlines()
        f_no_comments = []
        f_comments = []
        for line in f:
                c = -1
                i = "0"
                index = f.index(line)
                while (i != '#') & (c < len(line)-1):
                        c = c + 1
                        i = line[c]
                f_no_comments.append(line[0:c+1])
                if i == '#': f_comments.append(line[c:])

        return [f_no_comments,f_comments]
