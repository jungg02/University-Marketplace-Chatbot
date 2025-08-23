# University-Marketplace-Chatbot

## Overview and Approach
This chatbot is designed to aid users, both buyers and sellers, on a broad range of topics in utilising the student marketplace. Safety and security of students were placed on a high priority without compromising on user experience.

To review each component, simply click to open the corresponding files.

## Assumptions
- Assume that the context for this marketplace is set in Singapore.
- Assume that most universities in Singapore follow the same general guidelines on prohibited items in student accomodations.
- Assume that the marketplace already has an existing user base of both buyers and sellers from multiple universities.
- Assume that there is a team of human moderators ready to respond to any escalation of events.

## Time Allocation
| Segment | Time |
| -------- | ------- |
|  Prompt Design and Engineering | 45mins  |
| Golden Test Design | 30mins  |
|  Automation & Update Process | 30mins |
| Marketplace Domain Knowledge | 15mins |

## Future Actions
- Further support for more complex common marketplace issues such as "scalpers", "lowballing" and "ghosting" can be provided with further training to improve overall user experience.
- Use RAG and web scraper tool to continuously update the chatbot with new context on changes to dorm policies or for a more targeted response. (eg. hall-specific requests from NUS)
- Incorporate GenAI capabilites to generate higher quality responses.

## Personal Reflection
After completing this assessment, I felt that the most challenging part would be coming up with the update process and the automation pipeline. This was a relatively new topic to me at this point in time and so I had to do my own research and understand what are some of the processes used in the industry today when companies automate the update process of their web application or online services while keeping it available to users.

## Alternative Approaches Considered
- Immediate escalation of all alerts for increased safety and security measures - might cause overload with limited number of human moderators.
- Immediate account termination for policy violation - might overlook certain scenarios, leading to wrongful removal of accounts which may damage user experience.
- Chatbot to handle most disputes to relieve strain on human moderators - chatbot may not fully understand human nuances and intentions which may lead to wrong advice provided.

## Personal Experiences
My personal experience using NUS Marketplace is generally quite pleasant. Everyone on the Telegram groupchat are mostly understanding and friendly to their peers. However, I do hear of instances of my friends getting scammed or receiving products which quality is much worse than stated by the seller. There are also individuals who goes onto the marketplace to mess with others without actually trying to buy or sell anything. These issues harms the overall user experience and has led to some of my friends not using it anymore.
