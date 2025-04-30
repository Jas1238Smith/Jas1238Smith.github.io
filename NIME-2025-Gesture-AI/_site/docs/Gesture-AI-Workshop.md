<a name="top"></a>
# Gesture and AI Workshop
## New Interfaces for Musical Expression, June 24th-27, 2025

|[**Top**](#top)|[**Schedule**](#schedule)|[**Demo**](#demo)|[**Links**](#links) 

### Description
Generative AI models have been used to great effect in creating large amounts of music and audio for creative applications. There are challenges in using generative AI in live performances, such as high latency and lack of agency in terms of expressive input for a performer to provide a generative model. We aim to build AI-based NIMEs that support musicians creatively, rather than replacing their efforts during a performance.

This workshop will discuss recognizing human motions and gestures through a camera and real-time audio generation. We will also discuss the use of adaptive machine learning to enable a system to evolve alongside its user. This demonstration will include a live tutorial on the development of a camera-based gesture recognition application using popular frameworks and libraries.

### Time & Place 
Time: Monday, June 24th, 2025.
Place: Location TBA

### Organizers
[Postdoc Jason Smith](https://scholar.google.com/citations?user=1R0IoRMAAAAJ&hl=en) Jason Brent Smith is a Postdoctoral Scholar at the Northwestern University Department of Computer Science and a member of the Interactive Audio Lab. He completed his PhD in Music Technology at the Georgia Institute of Technology in Fall 2024. Jason's research, including his dissertation titled ``Human-AI Partnerships in Gesture-Controlled Interactive Music,'' has centered on using AI-based gestural recognition in systems for musical performance and how musicians perceive those systems as tools for musical expression or creatively autonomous partners \cite{smith2021effects, smith2022human, smith2023effects}. Jason has also performed research in gestural recognition for prosthetic limb control\footnote{\url{https://www.youtube.com/watch?v=UwsrzCVZAb8}} and the use of AI assistance in music composition and programming \cite{smith2020modeling, truesdell2021supporting}.
    
[Prof. Bryan Pardo](http://bryanpardo.com) \textbf{\href{https://bryan-pardo.github.io}{Bryan Pardo}} is a Professor of Computer Science at the Northwestern University Department of Computer Science. He directs the Interactive Audio Lab and is a co-director of Northwestern's \href{https://www.hci.northwestern.edu}{HCI+Design Center}. Recent works in generative modeling of music and gestural control of generative modeling include \href{https://arxiv.org/pdf/2412.08550}{Sketch2Sound} \cite{garcia2024sketch2sound} and \href{https://arxiv.org/pdf/2307.04686}{VampNet} \cite{garcia2023vampnet}.

### Motivation
Generative AI is the use of machine learning to create content based on based on training data. It has been used in a variety of artistic mediums, including the creation of stories \cite{chung2022talebrush}, video \cite{zhou2024survey}, and music composition and production \cite{atanackovic2024artificial}.

Generative AI has become an emerging presence in the music industry. Companies like Pandora and Spotify use AI to generate playlists \cite{thingstad2023impact}. Voice cloning systems are broadly used to duplicate a singer's signature sounds \cite{arik2018neural}. Google has created a series of experimental generative music models including MusicTransformer \cite{huang2018music} and MusicLM \cite{agostinelli2023musiclm}. More recently, companies such as Suno, Udio, and Stability AI have created consumer-facing systems that generate entire pop songs prompted by a single text phrase (e.g., "Write me a song about bananas.")

While the ability to create whole pieces of music conditioned on a single line of text is impressive, this level of control removes agency and expressive control from those using the system. These issues are compounded by the fact that generative AI models are designed to be used offline and cannot be used in live performances due to latency and the fact that they do not incorporate a performer's expression. This combination of non-real-time generation, controlled in only the most general terms by the users leaves many musicians and sound artists feeling disempowered and sidelined by these new tools.

Joint human-AI performances can combine the advantages of AI (creating large amounts of new music and sounds) with the artistic vision and deliberate expressions of a performing artist. When done properly, AI can support, rather than supplant, artists when used in a NIME powered by human input. Additionally, AI-based musical performance tools have the potential to benefit musicians with physical disabilities, as the tools provide the potential for expressive control gestures that work with rather than against the range of gestures a particular individual may be able to perform. This is in contrast to traditional instrument design, which is typically limited by the physical constraints of the musical instrument.

There are multiple forms of input to an interactive music system, but gesture has been linked to a user's intention in musical performance \cite{bevilacqua2007wireless} as well as an audience's understanding of the connections between movement and musical meaning \cite{camurri2003multimodal, camurri2005communicating}. Human movement gestures have long been used to generate audio for expressive performances \cite{wanderley2001gestural, wanderley2004gestural} and have been evaluated as components of NIMEs \cite{stowell2008discourse, jorda2014methodological}.

The use of gestures to control generative music and sound synthesis has evolved alongside NIME design and methods for capturing gestures. Earlier systems have used sensors and multitouch devices \cite{Wessel2009, Woldecke2010}, manual editing of audio parameters in software \cite{Keith2009, Brown2010}, and input through commercially-available MIDI interfaces \cite{Whalley2010}. Machine learning has been used alongside mounted hardware sensors \cite{jschacher2015, Schlei2016} and transducers \cite{aeldridge2017} to give generative NIMEs the affordances of existing, physical musical instruments. Advances in gesture recognition (such as object detection algorithms) have seen increased focus on interaction in generative NIMEs, between multiple humans whose input movements are recorded
\cite{NIME20_49} or interactive co-creation \cite{NIME20_12, smith2022human, nime2023_91} and demonstration \cite{NIME21_6} between human performer and AI component of a generative music system. Modern machine learning architectures have enabled live generation of unique musical sound based on various input gestures such as software instrument controls or physical movement recorded through cameras \cite{nime2023_90, nime2023_94, nime2024_39}. AI has also been used in the \textit{creation} of NIMEs, such as image-to-image translation for the development of new hardware interfaces \cite{VanTroyer2019}, and development of accessible musical instruments based on text-to-image generation \cite{nime2023_83}.

This workshop will focus on the real-time capture of gestures and mapping of those gestures to controls for neural audio synthesis. This year's NIME theme, Entangled NIME, asks authors to consider how musical interfaces can evolve with their users. This workshop will address this question through discussion and examples of adaptive machine learning behaviors designed to adjust a system's musical output based on gestures learned during a performance.

### Technical Requirements
This workshop will require a small to medium-sized lecture hall or a similar room. Although intended for in-person participants, the activities will be suitable for remote attendees. This event will be able to accommodate up to 20 participants. The venue will require a screen projector with an HDMI connection and powered speakers that can connect to the presenter's laptop. 

Participants are expected to bring their own computers (Linux, Windows, or MacOS). Their computers must have a camera, or they must bring an external camera to be used in gestural recognition. A development environment for Python (e.g. Anaconda), ready to be used, is also required: participants of all levels of experience with Python are welcome. Pure Data, a visual programming language suited for music and other multimedia performances, will also be used during the workshop. Although time will be allocated to set up Pure Data, participants will be encouraged to download the program before the workshop.

#### Schedule
<a name="schedule"></a>
### Workshop Schedule  

The workshop is scheduled for four hours.

|Time|Topic|
|40 minutes| Overview of machine learning and gesture control of sound synthesis in music performance. (40 minutes)
            \item A brief history of machine learning in NIME design and music performance (e.g. The Wekinator \cite{fiebrink2017machine}, RAVE \cite{caillon2021rave}, MusicLM \cite{agostinelli2023musiclm}, VampNet \cite{garcia2023vampnet})
            \item Cultural context, artists, and key systems for live gestural control of sound synthesis/manipulation (e.g. Imogen Heap, Zachary Lieberman, Holly Herndon, Laetitia Sonami, Pamela Z, Michel Waisvisz's The Hands)|
|90 minutes| Tutorial on developing a live camera-based gestural recognition tool in Python, using [Google MediaPipe](https://ai.google.dev/edge/mediapipe) to capture the movement of key points on a user's body |
| 20 minutes | Coffee Break |
| 45 minutes | Tutorial on developing using OSC communication from gestural recognition tool to live musical output in visual programming language [Pure Data](https://puredata.info/)|
|45 minutes | Tutorial on Online Machine Learning as a method of live adaptation to a user, including developing a live training loop in a camera-based application. |

### Demo Video
<a name="demo></a>
[Demo](https://bit.ly/gestalt-demo)

<a name="links"></a>
### Helpful Links

|[**Top**](#top)|[**Schedule**](#schedule)|[**Demo**](#demo)|[**Links**](#links) 