---
layout: default
title: Home
---

<a id="top"></a>
# Gesture and AI Workshop
## [New Interfaces for Musical Expression (NIME)](https://nime2025.org/), June 24th-27, 2025

|[**Top**](#top)|[**Schedule**](#schedule)|[**Demo**](#demo)|[**Links**](#links) 

## Description
Generative AI models have been used to great effect in creating large amounts of music and audio for creative applications. There are challenges in using generative AI in live performances, such as high latency and lack of agency in terms of expressive input for a performer to provide a generative model. We aim to build AI-based NIMEs that support musicians creatively, rather than replacing their efforts during a performance.

This workshop will discuss recognizing human motions and gestures through a camera and real-time audio generation. We will also discuss the use of adaptive machine learning to enable a system to evolve alongside its user. This demonstration will include a live tutorial on the development of a camera-based gesture recognition application using popular frameworks and libraries.

## Time & Place 
Time: June 24th, 2025.
Place: Location TBA

## Organizers
[Jason Smith](https://scholar.google.com/citations?user=1R0IoRMAAAAJ&hl=en) is a Postdoctoral Scholar at the Northwestern University Department of Computer Science and a member of the Interactive Audio Lab. He completed his PhD in Music Technology at the Georgia Institute of Technology in Fall 2024. Jason's research, including his dissertation titled ``Human-AI Partnerships in Gesture-Controlled Interactive Music,'' has centered on using AI-based gestural recognition in systems for musical performance and how musicians perceive those systems as tools for musical expression or [creatively](https://ojs.aaai.org/index.php/AIIDE/article/view/18895) [autonomous](https://dl.acm.org/doi/abs/10.1145/3581754.3584123) [partners](https://nime.pubpub.org/pub/2644jox5/release/1?readingCollection=bb45043c). Jason has also performed research in gestural recognition for [prosthetic limb control](https://www.youtube.com/watch?v=UwsrzCVZAb8) and the use of [modeling musical knowledge](https://ddmal.music.mcgill.ca/ISMIR-Conf/static/final_papers/326.pdf) for providing [AI assistantce](https://learndialogue.org/pdf/EarSketch_Griffith_ICCC_2021.pdf) to users of music composition and programming software.
    
[Bryan Pardo](http://bryanpardo.com) is a Professor of Computer Science at the Northwestern University Department of Computer Science. He directs the Interactive Audio Lab and is a co-director of Northwestern's [HCI+Design Center](https://www.hci.northwestern.edu). Recent works in generative modeling of music and gestural control of generative modeling include [Sketch2Sound](https://arxiv.org/pdf/2412.08550) and [VampNet](https://arxiv.org/pdf/2307.04686).

## Background
Generative AI is the use of machine learning to create content based on based on training data. It has been used in a variety of artistic mediums, including the creation of [stories](https://dl.acm.org/doi/abs/10.1145/3491102.3501819), [video](https://arxiv.org/abs/2404.16038), and [music composition and production](https://www.ceeol.com/search/article-detail?id=1299567).

Generative AI has become an emerging presence in the music industry. Companies like Pandora and Spotify use AI to generate [playlists](https://uia.brage.unit.no/uia-xmlui/handle/11250/3082199). Voice cloning systems are broadly used to duplicate a singer's [signature sounds](https://proceedings.neurips.cc/paper/2018/hash/4559912e7a94a9c32b09d894f2bc3c82-Abstract.html). Google has created a series of experimental generative music models including [Music Transformer](https://magenta.tensorflow.org/music-transformer) and [MusicLM](https://arxiv.org/abs/2301.11325). More recently, companies such as Suno, Udio, and Stability AI have created consumer-facing systems that generate entire pop songs prompted by a single text phrase (e.g., "Write me a song about bananas.")

While the ability to create whole pieces of music conditioned on a single line of text is impressive, this level of control removes agency and expressive control from those using the system. These issues are compounded by the fact that generative AI models are designed to be used offline and cannot be used in live performances due to latency and the fact that they do not incorporate a performer's expression. This combination of non-real-time generation, controlled in only the most general terms by the users leaves many musicians and sound artists feeling disempowered and sidelined by these new tools.

Joint human-AI performances can combine the advantages of AI (creating large amounts of new music and sounds) with the artistic vision and deliberate expressions of a performing artist. When done properly, AI can support, rather than supplant, artists when used in a NIME powered by human input. Additionally, AI-based musical performance tools have the potential to benefit musicians with physical disabilities, as the tools provide the potential for expressive control gestures that work with rather than against the range of gestures a particular individual may be able to perform. This is in contrast to traditional instrument design, which is typically limited by the physical constraints of the musical instrument.

This workshop will focus on the real-time capture of gestures and mapping of those gestures to controls for neural audio synthesis. This year's NIME theme, Entangled NIME, asks authors to consider how musical interfaces can evolve with their users. This workshop will address this question through discussion and examples of adaptive machine learning behaviors designed to adjust a system's musical output based on gestures learned during a performance.

# Schedule
<a id="schedule"></a>

The workshop is scheduled for four hours.

|Time|Topic|
|----------|----------|
|40 minutes| Overview of machine learning and gesture control of sound synthesis in music performance. A brief history of machine learning in NIME design and music performance (e.g. [The Wekinator](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=ced58510dbb49cc434d211092651d67aac030002), [RAVE](https://arxiv.org/abs/2111.05011), [MusicLM](https://arxiv.org/abs/2301.11325), [VampNet](https://arxiv.org/abs/2307.04686)). Cultural context, artists, and key systems for live gestural control of sound synthesis/manipulation (e.g. Imogen Heap, Zachary Lieberman, Holly Herndon, Laetitia Sonami, Pamela Z, Michel Waisvisz's The Hands).|
|90 minutes| Tutorial on developing a live camera-based gestural recognition tool in Python, using [Google MediaPipe](https://ai.google.dev/edge/mediapipe) to capture the movement of key points on a user's body |
| 20 minutes | Coffee Break |
| 45 minutes | Tutorial on developing using OSC communication from gestural recognition tool to live musical output in visual programming language [Pure Data](https://puredata.info/)|
|45 minutes | Tutorial on Online Machine Learning as a method of live adaptation to a user, including developing a live training loop in a camera-based application. |

# Demo Video
<a id="demo"></a>
[Demo](https://bit.ly/gestalt-demo)

## Technical Requirements
This workshop will require a small to medium-sized lecture hall or a similar room. Although intended for in-person participants, the activities will be suitable for remote attendees. This event will be able to accommodate up to 20 participants. The venue will require a screen projector with an HDMI connection and powered speakers that can connect to the presenter's laptop. 

Participants are expected to bring their own computers (Linux, Windows, or MacOS). Their computers must have a camera, or they must bring an external camera to be used in gestural recognition. A development environment for Python (e.g. Anaconda), ready to be used, is also required: participants of all levels of experience with Python are welcome. Pure Data, a visual programming language suited for music and other multimedia performances, will also be used during the workshop. Although time will be allocated to set up Pure Data, participants will be encouraged to download the program before the workshop.

# Links
<a id="links"></a>

## Tools & Development Environments
[Install Python](https://www.python.org)

[Install Pure Data](https://puredata.info)

[Install the Anaconda Python Development Environment](https://www.anaconda.com)

[Install the Visual Studio Code Development Environment](https://code.visualstudio.com)

## Readings: Gesture-Controlled NIMEs
### Gesture in Music Performance
[Wireless Sensor Interface and Gesture-Follower for Music Pedagogy](http://www.nime.org/proceedings/2007/nime2007_124.pdf)

[Multimodal Analysis of Expressive Gesture in Music and Dance Performances](https://link.springer.com/chapter/10.1007/978-3-540-24598-8_3)

[Communicating Expressiveness and Affect in Multimodal Interactive Systems](https://ieeexplore.ieee.org/abstract/document/1377101)

[Gestural Control of Music](http://recherche.ircam.fr/equipes/analyse-synthese/wanderle/Gestes/Externe/kassel.pdf)

[Gestural Control of Sound Synthesis](https://ieeexplore.ieee.org/abstract/document/1278687)

[Discourse Analysis Evaluation Method for Expressive Musical Interfaces](https://ualresearchonline.arts.ac.uk/id/eprint/23192/1/StowellPlumbley_nime08.pdf)

[A Methodological Framework for Teaching, Evaluating and Informing NIME Design with a Focus on Expressiveness and Mapping](https://www.nime.org/proceedings/2014/nime2014_472.pdf)

### Sensors and Multitiouch Devices
[Hands On --- A New Work from SLABS Controller and Generative Algorithms](https://www.nime.org/proceedings/2009/nime2009_335.pdf)

[Controlling Live Generative Electronic Music with Deviate](https://www.nime.org/proceedings/2009/nime2009_054.pdf)

[ANTracks 2.0 --- Generative Music on Multiple Multitouch Devices Categories and Subject Descriptors](https://www.nime.org/proceedings/2010/nime2010_348.pdf)

[Network Jamming: Distributed Performance using Generative Music](http://www.nime.org/proceedings/2010/nime2010_283.pdf)

[Generative Improv. & Interactive Music Project (GIIMP)](http://www.nime.org/proceedings/2010/nime2010_255.pdf)

### Generative NIMEs
[Gestural Electronic Music using Machine Learning as Generative Device](https://www.nime.org/proceedings/2015/nime2015_117.pdf)

[PourOver: A Sensor-Driven Generative Music Platform](https://www.nime.org/proceedings/2016/nime2016_paper0069.pdf)

[Self-resonating Feedback Cello: Interfacing gestural and generative processes in improvised performance](https://www.nime.org/proceedings/2017/nime2017_paper0005.pdf)

### Human-AI Interaction
[Crowd-driven Music: Interactive and Generative Approaches using Machine Vision and Manhattan](https://www.nime.org/proceedings/2020/nime2020_paper49.pdf)

[Composing computer generated music, an observational study using IGME: the Interactive Generative Music Environment](https://www.nime.org/proceedings/2020/nime2020_paper12.pdf)

[What to Play and How to Play it: Guiding Generative Music Models with Multiple Demonstrations](https://nime.pubpub.org/pub/s3x60926/release/1)

[Real-Time Co-Creation of Expressive Music Performances Using Speech and Gestures](https://nime.org/proceedings/2023/nime2023_91.pdf)

[SnakeSynth: New Interactions for Generative Audio Synthesis](https://nime.org/proceedings/2023/nime2023_90.pdf)

[Improvise+=Chain: Listening to the Ensemble Improvisation of an Autoregressive Generative Model](https://nime.org/proceedings/2023/nime2023_94.pdf)

[GrooveTransformer: A Generative Drum Sequencer Eurorack Module](https://nime.org/proceedings/2024/nime2024_39.pdf)

### AI in NIME Development
[From Mondrian to Modular Synth: Rendering NIME using Generative Adversarial Networks](https://www.nime.org/proceedings/2019/nime2019_paper052.pdf)

[Participatory Conceptual Design of Accessible Digital Musical Instruments using Generative AI](https://nime.org/proceedings/2023/nime2023_83.pdf)

|[**Top**](#top)|[**Schedule**](#schedule)|[**Demo**](#demo)|[**Links**](#links) 