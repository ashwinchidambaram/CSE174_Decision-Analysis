# Traffic Congestion at UCSC
This repository containts work related to project done in CSE 174, Decison Analysis, at UCSC.

## About this Project
UCSC has a population of about 20,000 students and staff going on campus everyday, 9000 of them live on campus and only have two roads access it. The future enrollment forecast estimates that there will be an additional 1000 students every year for the next 10 years. As off-campus students, we have experienced the effects of traffic congestion on campus that affect everybody, especially at peak hours. Our project deals with this major issue and we try to provide the best solution by applying all the concepts of decision analysis. 

### Proposed Alternative 1 - More Loop Busses on Campus
When traveling around the UCSC campus, the fastest way to get from one place to another is to ride one of the UCSC buses, called a Loop. Oftentimes during peak hours, there are not enough Loop buses for students to take. Therefore, students are forced to just take the first bus that they see, sometimes a Santa Cruz Metro bus. Having students on city buses just to travel around campus means that students who wish to go off campus often have to wait a long time for an
open city bus to take. Taking this into consideration, we believe our alternative of adding more loops during peak hours
will help to solve this problem.

### Proposed Alternative 2 - Priority Cards for Off-Campus Students @ UCSC
Perhaps the main reason why students drive to campus, increasing traffic congestion, as opposed to taking the Santa Cruz Metro buses is due to crowded buses that are constantly too full to pick up all passengers at a given stop. This unreliable system forces most students to drive so that they can efficiently travel to and from campus without wasting time. In order to ensure off-campus students can rely on the bus system, our group decided that giving them priority over on-campus students could help. To do this, we decided that a student could indicate they are off-campus in one of two possible ways: 

  1. Purchasing a premium card through UCSC, which would allow them to board the city buses before on-campus students.

  2. Obtaining free priority cards which would be subsidized by UCSC, allowing them to board city buses first. 

Ensuring that off-campus students board buses first, means that students would be able to rely more on the bus system so that they would not need to drive to campus. More students taking buses means less cars on campus and reduced traffic congestion.

### Proposed Alternative 3 - Selective Busstops for Metro Busses on Campus
On the UCSC campus, there are a few bus stops that are generally very busy with people getting both on and off the buses. We
believe that by establishing “selective” bus stops on campus where a metro bus will only selectively make stops might allow commuters to make it home easier while also enabling students on campus to traverse campus without too much of a hassle. Based on what we observed with students on campus in addition to our own experiences, students tend to opt for the bus even if it is simply to just get to the next bus stop, despite it being faster to walk there in comparison to waiting, boarding, and riding the bus. We can conclude that students will generally tend to choose the option which they perceive as easier and requires less effort. Seeing as this is the case, we would need to ensure that the bus stops are not adjacent to ensure that students are disincentivized to ride the bus to get around within campus.

**Role of csvmodifier.py and Data**
The data we collected from TAPS was also not very cleaned up due to the massive amount they gave us, so we had to clean the dataset ourselves. To do this, I wrote a custom Python script *csvmodifier.py* which was used to take a dataset with 990,722 data points, and cleaned to make it possible to import into pgAdmin. In pgAdmin, I created a new table in which we stored
all the data to be able to quickly pull any relevant information since it allows us to process lots of data in a relatively short amount of time.

## Conclusion
When folding back the decision tree, it was clear that the first alternative, adding more Loop buses, was the optimal alternative.

## Disclaimer
This project has been performed to the best of our knowledge and with limited resources and information. So by no means is this project a 100% accurate depiction of what the best alternative to solving Traffic Congestion is at UCSC. However, we have utilized as much of the data that was provided to us by the UCSC TAPS department to reach a reasonable conclusion. 
