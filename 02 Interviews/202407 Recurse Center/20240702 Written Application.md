# 20240702 Written Application

[What we look for](https://www.recurse.com/what-we-look-for)

## Questions

### Links

> Please include any that you have: GitHub, LinkedIn, personal website, etc.

GitHub: 
LinkedIn: 
Personal Website: 

### Code CracklePop

> Write a program that prints out the numbers 1 to 100 (inclusive). If the number is divisible by 3, print Crackle instead of the number. If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop. You can use any language.
<!--  -->
> Don’t submit a CracklePop without testing it to make sure it works. This shows carelessness and doesn’t give us confidence that you can program.

```py
i = 1

while i <= 100:
    isDivisibleBy5 = i % 5 == 0
    isDivisibleBy3 = i % 3 == 0

    if isDivisibleBy5 and isDivisibleBy3:
        print("CracklePop")
    elif isDivisibleBy5:
        print("Pop")
    elif isDivisibleBy3:
        print("Crackle")
    else:
        print(i)

    i += 1
```

[Permanent link on PythonTutor](https://pythontutor.com/render.html#code=i%20%3D%201%0A%0Awhile%20i%20%3C%3D%20100%3A%0A%20%20%20%20isDivisibleBy5%20%3D%20i%20%25%205%20%3D%3D%200%0A%20%20%20%20isDivisibleBy3%20%3D%20i%20%25%203%20%3D%3D%200%0A%0A%20%20%20%20if%20isDivisibleBy5%20and%20isDivisibleBy3%3A%0A%20%20%20%20%20%20%20%20print%28%22CracklePop%22%29%0A%20%20%20%20elif%20isDivisibleBy5%3A%0A%20%20%20%20%20%20%20%20print%28%22Pop%22%29%0A%20%20%20%20elif%20isDivisibleBy3%3A%0A%20%20%20%20%20%20%20%20print%28%22Crackle%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28i%29%0A%0A%20%20%20%20i%20%2B%3D%201&cumulative=false&curInstr=776&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

### Please link to a program you've written from scratch

> You can use something like GitHub's gist to host your code. It doesn't need to be long, but it should be something you've written yourself, and not using a framework (e.g., Rails). If you don't have anything to submit, code something small, like a game of tic-tac-toe.
<!--  -->
> Don’t paste the code of your program from scratch into the answer box on the application. Please link to it on GitHub or another website where it's hosted.

Hearthstone Card Random Generator. A few years ago when I first started learning web development.

At different jobs, I developed several mobile apps from scratch as a team, for example, a wine collection. These projects are cloned as private repos for personal reference while keeping confidentiality, but I'm happy to authorize access temporarily if anyone is interested.

```py
turn = 1
turns = {} 
mark = " "
mark1 = "X"
mark2 = "O"

grid = None
gridNum = 3
gridCol = "|"
gridRow = "-" * (gridNum * 2 - 1)

inputs = {}

def buildGrid():
    row = []
    map = []

    for i in range(gridNum):
        row.append(mark)
    for j in range(gridNum):
        map.append(row.copy())
    return map

def printGrid():
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if j < gridNum - 1: 
                print(value, end = gridCol)
            else:
                print(value)
            if i < gridNum - 1: 
                print(gridRow)

def placeMark():
    return

def checkGrid():
    turns[trun][coordinate] = None

    for i in range(gridNum):
        marksHorizontal = []
        marksVertical = []
        marksDiagonal = []

        for j in range(gridNum):
            marks

return

def startGame():
    grid = buildGrid()
    return

def resetGame():
    grid = buildGrid()
    return

def endGame():
    grid = None
    return

grid = buildGrid()
printGrid()
```

### What is the most fascinating thing you've learned in the past month?

> This doesn't have to be about programming.
<!-- > -->
> Don’t answer the “fascinating thing” question with something you learned about yourself. This doesn’t demonstrate intellectual curiosity, which is what this question is there to measure.
<!--  -->
> Your best opportunity to demonstrate this in your application is the question about the most fascinating thing you’ve learned recently. We want to hear about something surprising you learned, and it doesn’t need to be about programming. We’ve seen great answers to this question about everything from making jewelry to plant taxonomy to music theory.

Other than sex chromosomes, it may seem common sense to assume genetic contributions from father and mother are equivalent, but there is always an exception. Genomic imprinting is a natural phenomenon that suggests a sexual tug-of-war has been ongoing at the molecular level of the human species.

The core phase happens after fertilization when maternal and paternal genomes compete to imprint the DNA to regulate gene expression epigenetically. For example, DNA methylation turns the gene on and DNA demethylation turns the gene off.

Turned out that many imprinted genes are involved in growth and metabolism. Maternal imprinting reduces the growth of offspring by favoring uniform distribution of resources. In contrast, paternal imprinting promotes the growth of offspring by increasing the acquisition of nutrients from the mother. This constitutes the basis of Parental Conflict Theory, which proposes imprinting grew out of a competition between males for maternal resources.

This concept is consistent with classical natural selection and sperm competition. In some species, a female can mate more than once and have offspring from two or more males. If one father’s offspring grows larger than the rest, his offspring will be more likely to survive adulthood and pass along their genes.

More interestingly, this biased gene expression is only observed in mammals and seed plants, in which the development of fetuses and seeds depends solely on resources provided by the mother. However, such bias doesn’t occur in fish and birds, in which the amount of resources deposited in the egg is determined by the mother before fertilization. This is also true for egg-laying mammals, but not for pouched mammals.

The story does not end here. Since not all imprinted genes regulate growth, parental conflict theory does not apply to those cases. Many non-conflict theories have therefore been proposed. These alternative hypotheses may revise the entrenched view of kinship or sexual conflict in humans and other organisms.

### What do you want to be doing in two years?

I don't have a clear plan. My current goals are to secure a job with reasonable compensation and try the programming industry in the US. Different work culture, and respect for technical personnel. Nerdy is a negative in Hong Kong. Non-social. Doing?

### Why do you want to attend RC? How would attending RC be different than working on your own?

Coderbunker. 42 Fremount, Community. And I didn't know how to fully utilize the support. Re-ignite the passion for programming. Other than programming skills, challenge my people skills and how to be a good and pleasant person in general.

### What would you like to work on at RC?

> E.g. things you want to learn or understand better, projects you want to build or contribute to, etc. Consider where the edge of your abilities is, and where you’d like it to be at the end of your batch.

Practically, refresh and enhance programming skills to land a good developer job, preferably a company with a good culture and ethics. Full stack development, either web or mobile.

Otherwise, try to be open and see what existing projects interest me.

## Background

> This information will not disqualify your application. We use it to better get to know our applicants and where they currently are.

### Describe your programming background in a few sentences

From Hong Kong to New York, self-taught, community, consultant through agency, 

### Have you worked professionally as a programmer?

> If so, please describe your experience.

Yes, other than my resume. Disappointing, no pair programming, not even code review! Coding Mockey. Developer to management roles, or senior developers, whose workload is too heavy, let alone mentor junior developers.

### Do you have a Computer Science degree or are you seeking one?

No. Intensional choice. Not to downplay the value of a degree, but the ratio of the value is questionable. Otherwise Noble Table JavaScript bootcamp.

### What other commitments (work, life, family) would you have during your batch?

> RC is a full-time commitment, and we ask that you plan to participate Monday-Friday during our core hours (11 am - 5 pm ET).

Part-time Cantonese interpreter at CyraCom, but I can easily quit. 6 hours per day, I assume some people stay longer than that, right?
