from xml.etree import ElementTree
import glob
from testfall_cont import Gesamtprotokoll


class Testschritte(Gesamtprotokoll):

    def __init__(self):
        super().__init__()
        self.tree = []
        self.root = []
        self.text = None
        self.step_count = None
        self.tag = []

        path = r'filepath'
        for filename in glob.glob(path):
            with open(filename,'r') as f:
                tree = ElementTree.parse(f)
                self.tree.append(tree)
                root = tree.getroot()
                self.root.append(root)
                tag = root.tag
                self.tag.append(tag)
    # DB usage
    def test_steps(self):

        self.prop = list()
        self.indeces = list()
        i = 1
        for root in self.root:
            while root.find("./step[" + str(i) + "]"):
                self.steps = root.find("./step[" + str(i) + "]").attrib['count']
                #self.counts.append(self.steps)

                self.index = root.find("./step[" + str(i) + "]/prop[1]").text
                self.indeces.append(self.index)
                self.props = root.find("./step[" + str(i) + "]/prop[5]").text
                self.prop.append(self.props)

                i += 1


    def steps(self):

        self.pass_index = list()
        self.fail_index = list()
        self.blocked_index = list()
        self.counts = list()
        self.pass_ = list()
        self.fail_ = list()
        self.blocked_ = list()


        for root in self.root:
            i = 1

            while root.find("./step[" + str(i) + "]"):
                self.steps = root.find("./step[" + str(i) + "]").attrib['count']
                self.counts.append(self.steps)
                self.props = root.find("./step[" + str(i) + "]/prop[6]").text
                if self.props == "PASS":
                    self.index_pass = root.find("./step[" + str(i) + "]/prop[1]").text
                    self.pass_index.append(self.index_pass)
                    self.prop_pass = root.find("./step[" + str(i) + "]/prop[4]").text
                    self.pass_.append(self.prop_pass)
                elif self.props == "FAIL":
                    self.index_fail = root.find("./step[" + str(i) + "]/prop[1]").text
                    self.fail_index.append(self.index_fail)
                    self.prop_fail = root.find("./step[" + str(i) + "]/prop[4]").text
                    self.fail_.append(self.prop_fail)
                else:
                    self.index_block = root.find("./step[" + str(i) + "]/prop[1]").text
                    self.blocked_index.append(self.index_block)
                    self.prop_blocked = root.find("./step[" + str(i) + "]/prop[4]").text
                    self.blocked_.append(self.prop_blocked)


                i += 1

    def display(self):

        #print("Step Count:",self.counts)
        print("PASS Index",self.pass_index)
        print("PASS", self.pass_)
        print("FAIL Index",self.fail_index)
        print("FAIL", self.fail_)
        print("BLOCKED Index", self.blocked_index)
        print("BLOCKED",self.blocked_)
        # print("Index",self.indeces)
        # print("Step",self.prop)

if __name__ == '__main__':

    test = Testschritte()
    test.steps()
    test.display()

