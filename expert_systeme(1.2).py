import math
import itertools

class treenod():
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        self.children.append(child)
        child.parent=self
    

def build_tree():
    headache=treenod("headache")
    ff=treenod("fever_&_fatigue")
    nv1=treenod("nausea_&_vomiting G1")
    nv2=treenod("nausea_&_vomiting G2")
    dizz1=treenod("dizziness G1")
    dizz2=treenod("dizziness G2")
    dizz3=treenod("dizziness G3")
    dizz4=treenod("dizziness G4")
    dizz5=treenod("dizziness G5")
    diarrhea1=treenod("diarrhea G1")
    diarrhea2=treenod("diarrhea G2")
    diarrhea3=treenod("diarrhea G3")
    diarrhea4=treenod("diarrhea G4")
    cough1=treenod("cough G1")
    cough2=treenod("cough G2")

    headache.add_child(nv1)
    nv1.add_child(dizz1)
    dizz1.add_child(treenod("Stroke"))

    headache.add_child(ff)
    ff.add_child(cough1)
    cough1.add_child(treenod("Mononucleosis"))

    ff.add_child(nv2)
    nv2.add_child(treenod("Meningitis"))

    nv2.add_child(dizz2)
    dizz2.add_child(treenod("Encephalitis"))

    dizz2.add_child(diarrhea2)
    diarrhea2.add_child(treenod("Toxic Shock Syndrome"))

    nv2.add_child(diarrhea1)
    diarrhea1.add_child(dizz3)
    dizz3.add_child(treenod("Toxic Shock Syndrome"))
    diarrhea1.add_child(treenod("Stomach Flu"))

    nv2.add_child(cough2)
    cough2.add_child(treenod("Influenza"))

    cough2.add_child(dizz4)
    dizz4.add_child(treenod("Cancer"))

    dizz4.add_child(diarrhea4)
    diarrhea4.add_child(treenod("COVID-19"))

    cough2.add_child(diarrhea3)
    diarrhea3.add_child(treenod("Ehrlichiosis"))

    diarrhea3.add_child(dizz5)
    dizz5.add_child(treenod("COVID-19"))
    

    return headache

def comparison(node,symptom):
    L=node.split(" ")
    node=L[0]
    return(node==symptom)


def search(current_node,symptoms_list):
    no_conclusive_symptoms="the given symptoms list is not enough to recognize the disease"
    unidentified_path="the given symptoms list is longer than the followed path"
    #print("\n lenght of symptoms list"+str(len(symptoms_list)))
    if  not symptoms_list :
        for child_node in current_node.children:
            if not child_node.children:
                return (f"your disease is {child_node.data}")
        return(no_conclusive_symptoms)
    for Sy in symptoms_list:
        #print("\n new symptom test : "+Sy)
        if len(current_node.children )>0:
            for child in current_node.children:
                #print("\n new child test : "+child.data)
                if comparison(child.data,Sy):
                    symptoms_list.remove(Sy)
                    return search(child,symptoms_list)
        else:
            return(unidentified_path)
   
def sym():
    while True :
        print("available symptoms:[cough,diarrhea,dizziness,fatigue,fever,headache,nausea,vomiting]")
        ch=input("insert your symptoms : ")
        if ch!="":
            ch.strip(".").strip(" ").strip(",")
            L=ch.replace(",", " ").replace(".", " ").split(" ")
            Ld=[]
            Ls= ["cough", "diarrhea", "dizziness", "headache", "fatigue","fever", "nausea", "vomiting"]
            print()
            for sy in L:
                sy=sy.lower()
                if sy in Ls :
                    Ld.append(sy)
            if "fatigue" in Ld and "fever" in Ld:
                Ld.remove("fatigue")
                Ld.remove("fever")
                Ld.append("fever_&_fatigue")
            if "nausea" in Ld and "vomiting" in Ld:
                Ld.remove("nausea")
                Ld.remove("vomiting")
                Ld.append("nausea_&_vomiting")
            if Ld!=[]:
                print(Ld)
                assert "headache" in Ld,"sorry your diseas is not in my data"
                Ld.remove("headache")
                return(Ld)
            else :
                print("you didn't put any of the symptoms that are availble , try again please")
        else :
            print("u have put an empty message , try again please")


def combination (L):
    # Generate all permutations using itertools.permutations
    permutations = list(itertools.permutations(L))
    # Convert tuples to lists for better readability
    return [list(perm) for perm in permutations]
    
def Main():  
    no_conclusive_symptoms="the given symptoms list is not enough to recognize the disease"
    unidentified_path="the given symptoms list is longer than the followed path"
    headache=build_tree()
    Sy=sym()
    list_symptoms=combination(Sy)
    for symptoms in list_symptoms:
        disease=search(headache,symptoms)
        if disease!=no_conclusive_symptoms and disease!=unidentified_path and disease != None:
            break
    print(disease)


if __name__=="__main__":
    Main()
