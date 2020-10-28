import streamlit as st


def experiences():
    experiences = st.beta_expander("Experiences")
    experiences.markdown(
        " __2020__: PyTorch implementation of the paper \
        [Deep Attentive Features for Prostate Segmentation in 3D Transrectal Ultrasound.](https://arxiv.org/pdf/1907.01743.pdf)    \n"
        "Main concepts implemented:    \n"
        "   - Multi Head Attention    \n"
        "   - Feature Pyramid Network (FPN)    \n"
        "   - Atrous Spatial Pyramid Pooling (ASPP)")
    experiences.markdown(
        " __2020__: First experiments (at least to my knowledge) of \
        hepatic bile duct pathologies detection on \
        [SPYGLASS](https://www.bostonscientific.com/en-EU/products/direct-visualization-systems/spyglass-ds-direct-visualization-system.html) \
        videos.    \n"
        "Main concepts implemented:    \n"
        "   - Generic Encoder-Decoder framework    \n"
        "   - Video Dataloader    \n"
        "   - Frames fusion: first (again to my knowledge) public implementation of the paper \
            [Large-scale Video Classification with Convolutional Neural Networks](https://static.googleusercontent.com/media/research.google.com/fr//pubs/archive/42455.pdf).    \n"
        "   - ConvLSTM    \n"
        "   - Vision Transformers: Implementation of the paper (preprint, under review) \
            [An Image is worth 16x16 words: Transformers for image recognition at scale](https://arxiv.org/pdf/2010.11929.pdf). \
            Unfortunately i can't make this implementation public yet but I'll do it as soon as possible.")
    experiences.markdown(
        "__2020__: [DataChallenge](https://datachallenge.sfrnet.org/) for the French Radiology Society Congress. Subject: \
        Automatic assessment of severity of coronary artery disease through AI assisted \
        coronary artery calcium score computation.    \n"
        "Main concepts implemented:    \n"
        "   - 3D Pytorch Pipeline    \n"
        "   - Preprocessing on 3D volumes (scans and segmentation masks).    \n"
        "   - DeepLab  v3+ 3D from the paper 'Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation'.")
    experiences.markdown(
        "__2020__: [MicroNet Challenge](https://micronet-challenge.github.io/). The goal is to build the most efficient model \
        that solves the target task to the specified quality level. A baseline is given and the teams are ranked by a compression factor from \
        this baseline.    \n"
        "Main concepts implemented:    \n"
        "   - Generic Training pipeline allowing to test several training configurations, including activation function, \
        learning rate scheduler, optimizer, base network, losses.    \n"
        "   - Guided pruning through adaptative weight decay.    \n"
        "   - Quantization.    \n"
        "   - Graph knowledge distillation from the paper [Deep geometric knowledge distillation with graphs](https://arxiv.org/pdf/1911.03080.pdf).    \n"
        "   - Deep K-Mean    \n"
        "   - Spectral Clustering from the paper \
            [The p-value as a new similarity function for spectral clustering in sensor networks](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8450769)."
        "Compression factor obtained: ~ x300 (our arch is 300 times lighter than the baseline).")
    experiences.markdown(
        "__2018/2019__: Internship period at Gustave Roussy hospital (the first European Cancer Center). \
        Development of an end-to-end training pipeline for multi organ cancer detection. I focused on lung nodules \
        detection, and the API conception.")
    experiences.markdown(
    "__2018__: Collaboration with the Cavale Blanche hospital, Brest. Multi Organ Segmentation. \
        Conventional U-Net based architectures were used.")
        
def education():
    education = st.beta_expander("Educational Background")
    education.subheader("2017 - 2020: National Graduate Engineering School")
    education.write(
        "IMT Atlantique (ex Telecom Bretagne), from the national competitive examination \
        Mines-Ponts.    \n"
        "2nd year major: Machine Learning & Deep Learning.    \n"
        "3rd year major: Health Engineering.")
    education.subheader("2014 - 2017: Preparatory Classes")
    education.write(
        "Lycée Kléber, Strasbourg    \n"
        "Undergraduate intensive courses in mathematics, physics, and computer sciences \
        to prepare for the french 'Grandes Ecoles' national competitive examination.")
    education.subheader("2014: Scientific Baccalauréat")
    education.write(
        "Major in mathematics.    \n"
        "European Classes (advanced english course).    \n"
        "Fist class honours.")

def skills():
    skills = st.beta_expander("Main skills")
    left, right = skills.beta_columns([1,10])
    left.write("Python : ")
    right.progress(100)
    right.write("I've an advanced knowledge of Python, including object oriented programming \
    and design patterns.")
    left, right = skills.beta_columns([1,9])
    left.write("PyTorch : ")
    right.progress(90)
    right.write("I've a quite extensive understanding of PyTorch and its ecosystem.  \
        I usually like to work with PyTorch Lightning, which allows one to create \
        new, robust, and reproducible deep learning architectures very quickly.")
    left, right = skills.beta_columns([1,10])
    left.write("Linux : ")
    right.progress(80)
    right.write("Even though Linux understanding can always get deeper, I would say I'm a decent \
        Linux user.")
    left, right = skills.beta_columns([1,10])
    left.write("C : ")
    right.progress(60)
    right.write("I'm not a seasoned C programmer but I have a quite good knowledge of this language.")
    


def nonpro():
    nonpro = st.beta_expander("Non Professional")
    nonpro.subheader("2017: President of the Student Office")
    nonpro.write(
        "The Student Office is abose every clubs or assocations and acts as \
        an intermediate between the school administration and the students. It teaches me a lot \
        about public relations, teamworking, and projects management.")
    nonpro.subheader("2014: Concours Général de Philosophie")
    nonpro.write("During my final high school year, aside my preparation for the Baccalauréat, \
        I took park in the Concours Général de Philosophie.")
    nonpro.subheader("2007 - 2015: Member of the 'Scouts et Guides' de France.")
    nonpro.write(
        "I've been a member of the french scoutism movement for ten years. \
        I've also animated camp as a scoutmaster for 3 years, which gave me experiences \
        in project management and teamworking.")
    nonpro.subheader("2010 - 2014: Solidarity actions for homeless peoples. ")
    nonpro.write(
        "I've been a member of the assocation 'Saint Vincent de Paul'. \
        My weekly task was to talk with homeless people as well as giving them food \
        and habits. I've also done restoration works in social housing.")

def hobbies():
    hobbies = st.beta_expander("Hobbies")
    hobbies.write("I play the guitare and the piano. I also love reading and playing chess. \
        Obviously a lot more could be said here but that's most likely not why you're here.")


def content():
    st.title('Curriculum vitæ')
    experiences()
    education()
    skills()
    nonpro()
    hobbies()
    


