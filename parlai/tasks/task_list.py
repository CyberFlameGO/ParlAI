#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""
This file contains a list of all the tasks, their id and task name, description and the
tags associated with them.
"""

task_list = [
    {
        "id": "AmazonQA",
        "display_name": "AmazonQA",
        "task": "amazon_qa",
        "tags": ["QA"],
        "links": {"website": "http://jmcauley.ucsd.edu/data/amazon/qa/"},
        "description": (
            "This dataset contains Question and Answer data from Amazon, "
            "totaling around 1.4 million answered questions."
        ),
    },
    {
        "id": "AQuA",
        "display_name": "AQuA",
        "task": "aqua",
        "tags": ["QA"],
        "links": {"arXiv": "https://arxiv.org/abs/1705.04146"},
        "description": (
            "Dataset containing algebraic word problems with rationales for "
            "their answers."
        ),
    },
    {
        "id": "bAbI-1k",
        "display_name": "bAbI 1k",
        "task": "babi:All1k",
        "tags": ["QA"],
        "description": (
            "20 synthetic tasks that each test a unique aspect of text and "
            "reasoning, and hence test different capabilities of learning "
            "models."
        ),
        "links": {"arXiv": "http://arxiv.org/abs/1502.05698"},
        "notes": (
            "You can access just one of the bAbI tasks with e.g. "
            "'babi:Task1k:3' for task 3."
        ),
    },
    {
        "id": "bAbI-10k",
        "display_name": "bAbI 10k",
        "task": "babi:All10k",
        "tags": ["QA"],
        "description": (
            "20 synthetic tasks that each test a unique aspect of text and "
            "reasoning, and hence test different capabilities of learning "
            "models."
        ),
        "links": {"arXiv": "http://arxiv.org/abs/1502.05698"},
        "notes": (
            "You can access just one of the bAbI tasks with e.g. 'babi:Task10k:3' "
            "for task 3."
        ),
    },
    {
        "id": "BlendedSkillTalk",
        "display_name": "Blended Skill Talk",
        "task": "blended_skill_talk",
        "tags": ["ChitChat"],
        "description": (
            "A dataset of 7k conversations explicitly designed to exhibit multiple "
            "conversation modes: displaying personality, having empathy, and "
            "demonstrating knowledge."
        ),
    },
    {
        "id": "BookTest",
        "display_name": "BookTest",
        "task": "booktest",
        "tags": ["Cloze"],
        "description": (
            "Sentence completion given a few sentences as context from a book. "
            "A larger version of CBT."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1610.00956"},
    },
    {
        "id": "BotAdversarialDialogue",
        "display_name": "Bot Adversarial Dialogue ",
        "task": "bot_adversarial_dialogue",
        "tags": [],
        "description": (
            "Datasets described in the paper Recipes for Safety in Open-domain Chatbots. "
            "Datasets consist of classification tasks in which the goal is to "
            "determine if the utterance is offensive or not given a dialogue context. "
        ),
        "links": {"arXiv": "https://arxiv.org/abs/2010.07079"},
    },
    {
        "id": "CBT",
        "display_name": "Children's Book Test (CBT)",
        "task": "cbt",
        "tags": ["Cloze"],
        "description": (
            "Sentence completion given a few sentences as context from a "
            "children's book."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1511.02301"},
    },
    {
        "id": "CCPE",
        "display_name": "Coached Conversational Preference Elicitation",
        "task": "ccpe",
        "tags": ["Goal"],
        "description": (
            "A dataset consisting of 502 dialogs with 12,000 annotated "
            "utterances between a user and an assistant discussing movie "
            "preferences in natural language. It was collected using a "
            "Wizard-of-Oz methodology between two paid crowd-workers, "
            "where one worker plays the role of an 'assistant', while "
            "the other plays the role of a 'user'."
        ),
        "links": {
            "website": "https://ai.google/tools/datasets/coached-conversational-preference-elicitation"
        },
    },
    {
        "id": "CMU_DoG",
        "display_name": "CMU Document Grounded Conversations",
        "task": "cmu_dog",
        "tags": ["ChitChat", "Grounded"],
        "description": (
            "A document grounded dataset for text conversations, where the "
            "documents are Wikipedia articles about popular movies. Consists "
            "of 4112 conversations with an average of 21.43 turns per conversation."
        ),
        "links": {
            "arXiv": "https://arxiv.org/abs/1809.07358",
            "github": "https://github.com/festvox/datasets-CMU_DoG",
        },
    },
    {
        "id": "COPA",
        "display_name": "Choice of Plausible Alternatives",
        "task": "copa",
        "tags": ["Reasoning"],
        "description": (
            "The Choice Of Plausible Alternatives (COPA) evaluation provides "
            "researchers with a tool for assessing progress in open-domain "
            "commonsense causal reasoning. COPA consists of 1000 questions, "
            "split equally into development and test sets of 500 questions each."
        ),
        "links": {"website": "http://people.ict.usc.edu/~gordon/copa.html"},
    },
    {
        "id": "COQA",
        "display_name": "Conversational Question Answering Challenge",
        "task": "coqa",
        "tags": ["QA"],
        "description": (
            "CoQA is a large-scale dataset for building Conversational "
            "Question Answering systems. The goal of the CoQA challenge "
            "is to measure the ability of machines to understand a text "
            "passage and answer a series of interconnected questions that "
            "appear in a conversation. CoQA is pronounced as coca."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1808.07042"},
    },
    {
        "id": "CornellMovie",
        "display_name": "Cornell Movie",
        "task": "cornell_movie",
        "tags": ["ChitChat", "Dodeca"],
        "description": ("Fictional conversations extracted from raw movie scripts."),
        "links": {"arXiv": "https://arxiv.org/abs/1106.3077"},
    },
    {
        "id": "DBLL-bAbI",
        "display_name": "Dialog Based Language Learning: bAbI Task",
        "task": "dbll_babi",
        "tags": ["Goal"],
        "description": (
            "Short dialogs based on the bAbI tasks, but in the form of a "
            "question from a teacher, the answer from the student, and finally a "
            "comment on the answer from the teacher. The aim is to find learning "
            "models that use the comments to improve."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1604.06045"},
        "notes": (
            "Tasks can be accessed with a "
            "format like: 'parlai display_data -t "
            "dbll_babi:task:2_p0.5' which specifies task 2, and policy with 0.5 "
            "answers correct, see the paper for more details of the tasks."
        ),
    },
    {
        "id": "DBLL-Movie",
        "display_name": "Dialog Based Language Learning: WikiMovies Task",
        "task": "dbll_movie",
        "tags": ["Goal"],
        "description": (
            "Short dialogs based on WikiMovies, but in the form of a question "
            "from a teacher, the answer from the student, and finally a comment "
            "on the answer from the teacher. The aim is to find learning models "
            "that use the comments to improve."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1604.06045"},
    },
    {
        "id": "dialog-bAbI",
        "display_name": "Dialog bAbI",
        "task": "dialog_babi",
        "tags": ["Goal"],
        "description": "Simulated dialogs of restaurant booking",
        "links": {"arXiv": "https://arxiv.org/abs/1605.07683"},
    },
    {
        "id": "dialog-bAbI-plus",
        "display_name": "Dialog bAbI+",
        "task": "dialog_babi_plus",
        "tags": ["Goal"],
        "description": (
            "bAbI+ is an extension of the bAbI Task 1 dialogues with everyday "
            "incremental dialogue phenomena (hesitations, restarts, and "
            "corrections) which model the disfluencies and communication "
            "problems in everyday spoken interaction in real-world environments. "
        ),
        "links": {
            "website": (
                "https://www.researchgate.net/publication/"
                "319128941_Challenging_Neural_Dialogue_Models_with_Natural_"
                "Data_Memory_Networks_Fail_on_Incremental_Phenomena"
            ),
            "paper": "http://aclweb.org/anthology/D17-1235",
        },
    },
    {
        "id": "dialogue-nli",
        "display_name": "Dialogue NLI",
        "task": "dialogue_nli",
        "tags": ["ChitChat", "NLI"],
        "description": (
            "Dialogue NLI is a dataset that addresses the issue of consistency in "
            "dialogue models."
        ),
        "links": {
            "website": "https://wellecks.github.io/dialogue_nli/",
            "arXiv": "https://arxiv.org/abs/1811.00671",
        },
    },
    {
        "id": "dstc7",
        "display_name": "DSTC7 subtrack 1 - ubuntu",
        "task": "dstc7",
        "tags": ["ChitChat"],
        "description": (
            "DSTC7 is a competition which provided a dataset of dialogs very "
            "similar to the ubuntu dataset. In particular, the subtrack 1 "
            "consists in predicting the next utterance."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1901.03461"},
    },
    {
        "id": "FVQA",
        "display_name": "FVQA",
        "task": "fvqa",
        "tags": ["Visual"],
        "description": (
            "The FVQA, a VQA dataset which requires, and supports, much deeper "
            "reasoning. We extend a conventional visual question answering "
            "dataset, which contains image-question-answer triplets, through "
            "additional image-question-answer-supporting fact tuples. The "
            "supporting fact is represented as a structural triplet, such as "
            "<Cat,CapableOf,ClimbingTrees>."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1606.05433"},
    },
    {
        "id": "DealNoDeal",
        "display_name": "Deal or No Deal",
        "task": "dealnodeal",
        "tags": ["Negotiation"],
        "description": (
            "End-to-end negotiation task which requires two agents to agree on "
            "how to divide a set of items, with each agent assigning different "
            "values to each item."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1706.05125"},
    },
    {
        "id": "Glue",
        "display_name": "Glue",
        "task": "glue",
        "tags": [],
        "description": (
            "GLUE, the General Language Understanding Evaluation benchmark is "
            "a collection of resources for training, evaluating, and analyzing "
            "natural language understanding systems."
        ),
        "links": {
            "website": "https://gluebenchmark.com/",
            "website2": "https://huggingface.co/datasets/glue",
        },
    },
    {
        "id": "HotpotQA",
        "display_name": "HotpotQA",
        "task": "hotpotqa",
        "tags": ["QA"],
        "description": (
            "HotpotQA is a dataset for multi-hop question answering. "
            "The overall setting is that given some context paragraphs"
            "(e.g., a few paragraphs, or the entire Web) and a question,"
            "a QA system answers the question by extracting a span of text"
            "from the context. It is necessary to perform multi-hop reasoning"
            "to correctly answer the question."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1809.09600"},
    },
    {
        "id": "HuggingFace",
        "display_name": "HuggingFace",
        "task": "huggingface",
        "tags": [],
        "description": ("HuggingFace datasets"),
        "links": {"website": "https://huggingface.co/"},
    },
    {
        "id": "LIGHT-Dialogue",
        "display_name": "LIGHT-Dialogue",
        "task": "light_dialog",
        "tags": ["Grounded", "Dodeca"],
        "description": (
            "LIGHT is a text adventure game with actions and dialogue collected. "
            "The source data is collected between crowdworkers playing the game."
        ),
        "links": {
            "website": "http://parl.ai/projects/light",
            "arXiv": "https://arxiv.org/abs/1903.03094",
        },
    },
    {
        "id": "LIGHT-Dialogue-Wild",
        "display_name": "LIGHT-Dialogue-Wild",
        "task": "light_dialog_wild",
        "tags": ["Grounded", "LIGHT"],
        "description": (
            " LIGHT is a text adventure game with actions and dialogue. "
            "The WILD dataset here features 41,131+ training episodes of dialogue "
            "collected from deploying a game as described in "
        ),
        "links": {
            "arXiv": "https://arxiv.org/abs/2008.08076",
            "website": "http://parl.ai/projects/light",
        },
    },
    {
        "id": "MutualFriends",
        "display_name": "MutualFriends",
        "task": "mutualfriends",
        "tags": ["Goal"],
        "description": (
            "Task where two agents must discover which friend of theirs is "
            "mutual based on the friends's attributes."
        ),
        "links": {"website": "https://stanfordnlp.github.io/cocoa/"},
    },
    {
        "id": "MCTest",
        "display_name": "MCTest",
        "task": "mctest",
        "tags": ["QA"],
        "description": ("Questions about short children's stories."),
        "links": {
            "website": (
                "https://www.microsoft.com/en-us/research/publication/"
                "mctest-challenge-dataset-open-domain-machine-comprehension-text/"
            )
        },
    },
    {
        "id": "MovieDD-QA",
        "display_name": "Movie Dialog QA",
        "task": "moviedialog:Task:1",
        "tags": ["QA", "MovieDD"],
        "description": (
            "Closed-domain QA dataset asking templated questions about movies, "
            "answerable from Wikipedia, similar to WikiMovies."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1511.06931"},
    },
    {
        "id": "MovieDD-QARecs",
        "display_name": "Movie Dialog QA Recommendations",
        "task": "moviedialog:Task:3",
        "tags": ["Goal", "MovieDD"],
        "description": (
            "Dialogs discussing questions about movies as well as recommendations."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1511.06931"},
    },
    {
        "id": "MovieDD-Recs",
        "display_name": "Movie Dialog Recommendations",
        "task": "moviedialog:Task:2",
        "tags": ["QA", "MovieDD"],
        "description": ("Questions asking for movie recommendations."),
        "links": {"arXiv": "https://arxiv.org/abs/1511.06931"},
    },
    {
        "id": "MovieDD-Reddit",
        "display_name": "Movie Dialog Reddit",
        "task": "moviedialog:Task:4",
        "tags": ["ChitChat", "MovieDD"],
        "description": (
            "Dialogs discussing Movies from Reddit (the Movies SubReddit)."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1511.06931"},
    },
    {
        "id": "MTurkWikiMovies",
        "display_name": "MTurk WikiMovies",
        "task": "mturkwikimovies",
        "tags": ["QA"],
        "description": (
            "Closed-domain QA dataset asking MTurk-derived questions about "
            "movies, answerable from Wikipedia."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1611.09823"},
    },
    {
        "id": "MultiNLI",
        "display_name": "MultiNLI",
        "task": "multinli",
        "tags": ["Entailment", "decanlp"],
        "description": (
            "A dataset designed for use in the development and evaluation of "
            "machine learning models for sentence understanding. Each example "
            "contains a premise and hypothesis. Model has to predict whether "
            "premise and hypothesis entail, contradict or are neutral to each "
            "other."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1704.05426"},
    },
    {
        "id": "NarrativeQA",
        "display_name": "NarrativeQA",
        "task": "narrative_qa",
        "tags": ["QA"],
        "description": (
            "A dataset and set of tasks in which the reader must answer "
            "questions about stories by reading entire books or movie scripts. "
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1712.07040"},
        "notes": (
            "You can access summaries only task for NarrativeQA by using task "
            "'narrative_qa:summaries'. By default, only stories are provided."
        ),
    },
    {
        "id": "NaturalQuestions",
        "display_name": "Natural Questions",
        "task": "natural_questions",
        "tags": ["QA"],
        "description": (
            "An open domain question answering dataset. "
            "Each example contains real questions that people searched "
            "for in Google and the content of the a Wikipedia article that "
            "was amongst the top 5 search resutls for that query, "
            "and its annotations. The annotations have the options of a long "
            "answer that is seleced from span of major content entities in "
            "the Wikipedia article (e.g., paragraphs, tables), a short answer"
            "that is selected from one or more short span of words in the "
            "article, or 'yes/no'. The existence of any of these answer "
            "formats depends on whether the main question can be answered, "
            "given the article; if not they are left empty."
        ),
        "links": {
            "paper": "https://research.google/pubs/pub47761/",
            "website": "https://ai.google.com/research/NaturalQuestions",
        },
        "notes": (
            "Since this task uses ChunkTeacher, it should be used with streaming."
        ),
    },
    {
        "id": "OpenSubtitles",
        "display_name": "Open Subtitles",
        "task": "opensubtitles",
        "tags": ["ChitChat"],
        "description": "Dataset of dialogs from movie scripts.",
        "links": {
            "version 2018 website": "http://opus.lingfil.uu.se/OpenSubtitles2018.php",
            "version 2009 website": "http://opus.lingfil.uu.se/OpenSubtitles.php",
            "related work (arXiv)": "https://arxiv.org/abs/1506.05869",
        },
    },
    {
        "id": "personalized-dialog-full",
        "display_name": "Personalized Dialog Full Set",
        "task": "personalized_dialog:AllFull",
        "tags": ["Goal", "Personalization"],
        "description": (
            "Simulated dataset of restaurant booking focused on personalization "
            "based on user profiles."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1706.07503"},
    },
    {
        "id": "personalized-dialog-small",
        "display_name": "Personalized Dialog Small Set",
        "task": "personalized_dialog:AllSmall",
        "tags": ["Goal", "Personalization"],
        "description": (
            "Simulated dataset of restaurant booking focused on personalization "
            "based on user profiles."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1706.07503"},
    },
    {
        "id": "QACNN",
        "display_name": "QA CNN",
        "task": "qacnn",
        "tags": ["Cloze"],
        "description": (
            "Cloze dataset based on a missing (anonymized) entity phrase from a "
            "CNN article"
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1506.03340"},
    },
    {
        "id": "QADailyMail",
        "display_name": "QA Daily Mail",
        "task": "qadailymail",
        "tags": ["Cloze"],
        "description": (
            "Cloze dataset based on a missing (anonymized) entity phrase from a "
            "Daily Mail article."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1506.03340"},
    },
    {
        "id": "QuAC",
        "display_name": "Question Answering in Context",
        "task": "quac",
        "tags": ["QA"],
        "description": (
            "Question Answering in Context is a dataset for modeling, "
            "understanding, and participating in information seeking dialog. Data "
            "instances consist of an interactive dialog between two crowd workers: "
            "(1) a student who poses a sequence of freeform questions to learn as "
            "much as possible about a hidden Wikipedia text, and (2) a teacher who "
            "answers the questions by providing short excerpts (spans) from the text. "
            "QuAC introduces challenges not found in existing machine comprehension "
            "datasets: its questions are often more open-ended, unanswerable, "
            "or only meaningful within the dialog context."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1808.07036"},
    },
    {
        "id": "SimpleQuestions",
        "display_name": "Simple Questions",
        "task": "simplequestions",
        "tags": ["QA"],
        "description": ("Open-domain QA dataset based on Freebase triples."),
        "links": {"arXiv": "https://arxiv.org/abs/1506.02075"},
    },
    {
        "id": "SNLI",
        "display_name": "The Stanford Natural Language Inference (SNLI) Corpus",
        "task": "snli",
        "tags": ["Entailment"],
        "description": (
            "The SNLI corpus (version 1.0) is a collection of 570k "
            "human-written English sentence pairs manually labeled for balanced "
            "classification with the labels entailment, contradiction, and "
            "neutral, supporting the task of natural language inference (NLI), "
            "also known as recognizing textual entailment (RTE)"
        ),
        "links": {"website": "https://nlp.stanford.edu/projects/snli/"},
    },
    {
        "id": "SQuAD2",
        "display_name": "SQuAD2",
        "task": "squad2",
        "tags": ["QA"],
        "description": (
            "Open-domain QA dataset answerable from a given paragraph from "
            "Wikipedia."
        ),
        "links": {"arXiv": "http://arxiv.org/abs/1806.03822"},
    },
    {
        "id": "SQuAD",
        "display_name": "SQuAD",
        "task": "squad",
        "tags": ["QA"],
        "description": (
            "Open-domain QA dataset answerable from a given paragraph from "
            "Wikipedia."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1606.05250"},
    },
    {
        "id": "SuperGLUE",
        "display_name": "SuperGLUE",
        "task": "superglue",
        "tags": [],
        "description": (
            "SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark "
            "styled after GLUE with a new set of more difficult language "
            "understanding tasks, improved resources, and a new public "
            "leaderboard."
        ),
        "links": {
            "website": "https://super.gluebenchmark.com/",
            "website2": "https://huggingface.co/datasets/super_glue",
        },
    },
    {
        "id": "TriviaQA",
        "display_name": "TriviaQA",
        "task": "triviaqa",
        "tags": ["QA"],
        "description": (
            "Open-domain QA dataset with question-answer-evidence triples."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1705.03551"},
    },
    {
        "id": "TaskNTalk",
        "display_name": "Task N' Talk",
        "task": "taskntalk",
        "tags": ["Goal"],
        "description": (
            "Dataset of synthetic shapes described by attributes, for agents to "
            "play a cooperative QA game."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1706.08502"},
    },
    {
        "id": "Ubuntu",
        "display_name": "Ubuntu",
        "task": "ubuntu",
        "tags": ["ChitChat", "Dodeca"],
        "description": (
            "Dialogs between an Ubuntu user and an expert trying to fix issue, "
            "we use the V2 version, which cleaned the data to some extent. "
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1506.08909."},
    },
    {
        "id": "WebQuestions",
        "display_name": "Web Questions",
        "task": "webquestions",
        "tags": ["QA"],
        "description": ("Open-domain QA dataset from Web queries."),
        "links": {"paper": "http://www.aclweb.org/anthology/D13-1160"},
    },
    {
        "id": "WikiMovies",
        "display_name": "WikiMovies",
        "task": "wikimovies",
        "tags": ["QA"],
        "description": (
            "Closed-domain QA dataset asking templated questions about movies, "
            "answerable from Wikipedia."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1606.03126"},
    },
    {
        "id": "WikiQA",
        "display_name": "WikiQA",
        "task": "wikiqa",
        "tags": ["QA"],
        "description": ("Open domain QA from Wikipedia dataset"),
        "links": {
            "website": (
                "https://www.microsoft.com/en-us/research/publication/wikiqa-a-"
                "challenge-dataset-for-open-domain-question-answering/"
            )
        },
    },
    {
        "id": "VQAv1",
        "display_name": "VQAv1",
        "task": "vqa_v1",
        "tags": ["Visual"],
        "description": ("Open-ended question answering about visual content."),
        "links": {"arXiv": "https://arxiv.org/abs/1505.00468"},
    },
    {
        "id": "VQAv2",
        "display_name": "VQAv2",
        "task": "vqa_v2",
        "tags": ["Visual"],
        "description": ("Bigger, more balanced version of the original VQA dataset."),
        "links": {"arXiv": "https://arxiv.org/abs/1612.00837"},
    },
    {
        "id": "VisDial",
        "display_name": "VisDial",
        "task": "visdial",
        "tags": ["Visual"],
        "description": (
            "Task which requires agents to hold a meaningful dialog about "
            "visual content."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1611.08669"},
    },
    {
        "id": "MNIST_QA",
        "display_name": "MNIST_QA",
        "task": "mnist_qa",
        "tags": ["Visual"],
        "description": (
            "Task which requires agents to identify which number they are "
            "seeing. From the MNIST dataset."
        ),
    },
    {
        "id": "InsuranceQA",
        "display_name": "InsuranceQA",
        "task": "insuranceqa",
        "tags": ["QA"],
        "description": (
            "Task which requires agents to identify high quality answers "
            "composed by professionals with deep domain knowledge."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1508.01585"},
    },
    {
        "id": "MS_MARCO",
        "display_name": "MS_MARCO",
        "task": "ms_marco",
        "tags": ["QA"],
        "description": (
            "A large scale Machine Reading Comprehension Dataset with questions "
            "sampled from real anonymized user queries and contexts from web "
            "documents."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1611.09268"},
    },
    {
        "id": "CLEVR",
        "display_name": "CLEVR",
        "task": "clevr",
        "tags": ["Visual"],
        "description": (
            "A visual reasoning dataset that tests abilities such as attribute "
            "identification, counting, comparison, spatial relationships, and "
            "logical operations."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1612.06890"},
    },
    {
        "id": "nlvr",
        "display_name": "nlvr",
        "task": "nlvr",
        "tags": ["Visual"],
        "description": (
            "Cornell Natural Language Visual Reasoning (NLVR) is a language "
            "grounding dataset based on  pairs of natural language statements "
            "grounded in synthetic images."
        ),
        "links": {"website": "http://lic.nlp.cornell.edu/nlvr/"},
    },
    {
        "id": "WMT",
        "display_name": "WMT",
        "task": "wmt",
        "tags": ["MT"],
        "description": (
            "Workshop on Machine Translation task, currently only includes en_de."
        ),
    },
    {
        "id": "IWSLT14",
        "display_name": "IWSLT14",
        "task": "iwslt14",
        "tags": ["MT", "decanlp"],
        "description": (
            "2014 International Workshop on Spoken Language task, currently "
            "only includes en_de and de_en."
        ),
        "links": {"website": "https://wit3.fbk.eu"},
    },
    {
        "id": "ConvAI2",
        "display_name": "ConvAI2",
        "task": "convai2",
        "tags": ["ChitChat", "Dodeca"],
        "description": (
            "A chit-chat dataset based on PersonaChat for a NIPS 2018 competition. "
        ),
        "links": {
            "arXiv": "https://arxiv.org/abs/1801.07243",
            "website": "http://convai.io/",
        },
    },
    {
        "id": "ConvAI_ChitChat",
        "display_name": "ConvAI_ChitChat",
        "task": "convai_chitchat",
        "tags": ["ChitChat", "decanlp"],
        "description": (
            "Human-bot dialogues containing free discussions of randomly chosen "
            "paragraphs from SQuAD."
        ),
        "links": {"website": "http://convai.io/data/"},
    },
    {
        "id": "Dialogue_QE",
        "display_name": "Dialogue_QE",
        "task": "dialogue_qe",
        "tags": [],
        "description": (
            "Human-bot dialogues labelled for quality at the level of "
            "dialogues. Can be used to train dialogue-level metric for dialogue "
            "systems."
        ),
    },
    {
        "id": "QAngaroo",
        "display_name": "QAngaroo",
        "task": "qangaroo",
        "tags": ["QA"],
        "description": (
            "Reading Comprehension with Multiple Hop. Including two datasets: "
            "WIKIHOP built on on wikipedia, MEDHOP built on paper abstracts from "
            "PubMed."
        ),
        "links": {"website": "http://qangaroo.cs.ucl.ac.uk/"},
    },
    {
        "id": "SCAN",
        "display_name": "SCAN",
        "task": "scan",
        "tags": ["Goal"],
        "description": (
            "SCAN is a set of simple language-driven navigation tasks for "
            "studying compositional learning and zero-shot generalization. The "
            "SCAN tasks were inspired by the CommAI environment, which is the "
            "origin of the acronym (Simplified versions of the CommAI Navigation "
            "tasks)."
        ),
        "links": {
            "arXiv": "https://arxiv.org/abs/1711.00350",
            "website": "https://github.com/brendenlake/SCAN",
        },
    },
    {
        "id": "Persona-Chat",
        "display_name": "Persona-Chat",
        "task": "personachat",
        "tags": ["ChitChat"],
        "description": (
            "A chit-chat dataset where paired Turkers are given assigned "
            "personas and chat to try to get to know each other."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1801.07243"},
    },
    {
        "id": "TaskMaster",
        "display_name": "TaskMaster-1-2019",
        "task": "taskmaster",
        "tags": ["ChitChat"],
        "description": (
            "A chit-chat dataset by GoogleAI providing high quality goal-oriented conversations"
            "The dataset hopes to provoke interest in written vs spoken language"
            "Both the datasets consists of two-person dialogs:"
            "Spoken: Created using Wizard of Oz methodology. "
            "Written: Created by crowdsourced workers who were asked to write the "
            "full conversation themselves playing roles of both the user and assistant."
        ),
        "links": {"website": "https://ai.google/tools/datasets/taskmaster-1"},
    },
    {
        "id": "Twitter",
        "display_name": "Twitter",
        "task": "twitter",
        "tags": ["ChitChat", "Dodeca"],
        "description": (
            "Twitter data found on GitHub. No "
            "train/valid/test split was provided so 10k for valid and 10k for "
            "test was chosen at random."
        ),
        "links": {"website": "https://github.com/Marsan-Ma/chat_corpus/"},
    },
    {
        "id": "Wikipedia",
        "display_name": "Wikipedia",
        "task": 'wikipedia',
        "tags": [],
        "description": ("Dump of Wikipedia articles from 2/3/18"),
        "notes": (
            "Specify ':full' for the full articles to be returned, otherwise "
            "defaults to ':summary', which provides the first paragraphs. To put "
            "the article in the labels and the title in the text, specify "
            "':key-value' at the end (for a title/content key-value "
            "association)"
        ),
    },
    {
        "id": "Flickr30k",
        "display_name": "Flickr30k",
        "task": "flickr30k",
        "tags": ["Visual"],
        "description": ("30k captioned images pulled from Flickr compiled by UIUC. "),
        "links": {
            "website": "http://web.engr.illinois.edu/~bplumme2/Flickr30kEntities/",
            "paper1": "https://arxiv.org/abs/1505.04870v2",
            "paper2": "http://aclweb.org/anthology/Q14-1006",
        },
    },
    {
        "id": "COCO_Captions",
        "display_name": "COCO_Captions",
        "task": "coco_caption",
        "tags": ["Visual"],
        "description": (
            "COCO annotations derived from the 2015 COCO Caption Competition. "
        ),
        "links": {"website": "http://cocodataset.org/"},
    },
    {
        "id": "integration_tests",
        "display_name": "Integration Tests",
        "task": "integration_tests",
        "tags": ["Debug"],
        "description": ("Artificial tasks for ensuring models perform as expected"),
    },
    {
        "id": "ConvAI2_wild_evaluation",
        "display_name": "ConvAI2_wild_evaluation",
        "task": "convai2_wild_evaluation",
        "tags": ["ChitChat"],
        "description": (
            "Dataset collected during the wild evaluation of ConvaAI2 participants "
            "bots. 60% train, 20% valid and 20% test is chosen at "
            "random from the whole dataset."
        ),
        "links": {"website": "http://convai.io"},
    },
    {
        "id": "sst",
        "display_name": "SST Sentiment Analysis",
        "task": "sst",
        "tags": ["decanlp"],
        "description": (
            "Dataset containing sentiment trees of movie reviews. We use the modified "
            "binary sentence analysis subtask given by the DecaNLP paper here."
        ),
        "links": {
            "website": "https://nlp.stanford.edu/sentiment/index.html",
            "website2": "https://github.com/openai/generating-reviews-discovering-sentiment/",
        },
    },
    {
        "id": "cnn_dm",
        "display_name": "CNN/DM Summarisation",
        "task": "cnn_dm",
        "tags": ["decanlp"],
        "description": (
            "Dataset collected from CNN and the Daily Mail with summaries as labels, "
            "Implemented as part of the DecaNLP task."
        ),
        "links": {"website": "https://cs.nyu.edu/~kcho/DMQA/"},
    },
    {
        "id": "qasrl",
        "display_name": "QA-SRL Semantic Role Labeling",
        "task": "qasrl",
        "tags": ["decanlp"],
        "description": ("QA dataset implemented as part of the DecaNLP task."),
        "links": {"website": "https://dada.cs.washington.edu/qasrl/"},
    },
    {
        "id": "qazre",
        "display_name": "QA-ZRE Relation Extraction",
        "task": "qazre",
        "tags": ["decanlp"],
        "description": (
            "Zero Shot relation extraction task implemented as part of the DecaNLP "
            "task."
        ),
        "links": {"website": "http://nlp.cs.washington.edu/zeroshot/"},
    },
    {
        "id": "woz",
        "display_name": "WOZ restuarant reservation (Goal-Oriented Dialogue)",
        "task": "woz",
        "tags": ["decanlp"],
        "description": (
            "Dataset containing dialogues dengotiating a resturant reservation. "
            "Implemented as part of the DecaNLP task, focused on the change "
            "in the dialogue state."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1604.04562"},
    },
    {
        "id": "wikisql",
        "display_name": "WikiSQL semantic parsing task",
        "task": "wikisql",
        "tags": ["decanlp"],
        "description": (
            "Dataset for parsing sentences to SQL code, given a table. "
            "Implemented as part of the DecaNLP task."
        ),
        "links": {"website": "https://github.com/salesforce/WikiSQL"},
    },
    {
        "id": "mwsc",
        "display_name": "MWSC pronoun resolution",
        "task": "mwsc",
        "tags": ["decanlp"],
        "description": (
            "Resolving possible ambiguous pronouns. "
            "Implemented as part of the DecaNLP "
            "task, and can be found on the decaNLP github."
        ),
        "links": {"website": "https://github.com/salesforce/decaNLP"},
    },
    {
        "id": "decanlp",
        "display_name": "DecaNLP: The Natural Language Decathlon",
        "task": "decanlp",
        "tags": [],
        "description": (
            "A collection of 10 tasks (SQuAD, IWSLT, CNN/DM, MNLI, SST, QA‑SRL,"
            "QA‑ZRE, WOZ, WikiSQL and MWSC) designed to challenge a model with a range "
            "of different tasks. Note that we use IWSLT 2014 instead of "
            "2016/2013test/2014test for train/dev/test as given in the DecaNLP paper. "
        ),
        "links": {
            "arXiv": "https://arxiv.org/abs/1806.08730",
            "github": "https://github.com/salesforce/decaNLP",
        },
    },
    {
        "id": "Personality_Captions",
        "display_name": "Personality_Captions",
        "task": "personality_captions",
        "tags": ["Visual"],
        "description": (
            "200k images from the YFCC100m dataset "
            "with captions conditioned on one of 215 personalities."
        ),
        "links": {
            "website": "https://multimediacommons.wordpress.com/yfcc100m-core-dataset/",
            "arXiv": "https://arxiv.org/abs/1810.10665",
        },
        "notes": (
            "If you have already downloaded the images, please specify with "
            "the `--yfcc-path` flag, as the image download script takes a "
            "very long time to run"
        ),
    },
    {
        "id": "Image_Chat",
        "display_name": "Image_Chat",
        "task": "image_chat",
        "tags": ["Visual", "ChitChat"],
        "description": (
            "202k dialogues and 401k utterances over 202k images from "
            "the YFCC100m dataset "
            "using 215 possible personality traits"
        ),
        "links": {
            "website": "https://klshuster.github.io/image_chat/",
            "website2": "https://multimediacommons.wordpress.com/yfcc100m-core-dataset/",
        },
        "notes": (
            "If you have already downloaded the images, please specify with "
            "the `--yfcc-path` flag, as the image download script takes a "
            "very long time to run"
        ),
    },
    {
        "id": "Image_Chat_Generation",
        "display_name": "Image_Chat_Generation",
        "task": "image_chat:Generation",
        "tags": ["Visual", "ChitChat", "Dodeca"],
        "description": ("Image Chat task to train generative model"),
    },
    {
        "id": "Wizard_of_Wikipedia",
        "display_name": "Wizard_of_Wikipedia",
        "task": "wizard_of_wikipedia",
        "tags": ["ChitChat"],
        "description": (
            "A dataset with conversations directly grounded with knowledge "
            "retrieved from Wikipedia. Contains 201k utterances from 22k "
            "dialogues spanning over 1300 diverse topics, split into train, "
            "test, and valid sets. The test and valid sets are split "
            "into two sets each: one with overlapping topics with the train "
            "set, and one with unseen topics."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1811.01241"},
        "notes": (
            "To access the different valid/test splits (unseen/seen), specify "
            "the corresponding split (`random_split` for seen, `topic_split` "
            "for unseen) after the last colon in the task. "
            "E.g. `wizard_of_wikipedia:WizardDialogKnowledgeTeacher:random_split`"
        ),
    },
    {
        "id": "Wizard_of_Wikipedia_Generator",
        "display_name": "Wizard_of_Wikipedia_Generator",
        "task": "wizard_of_wikipedia:Generator",
        "tags": ["ChitChat", "Dodeca"],
        "description": ("Wizard of Wikipedia task to train generative models"),
    },
    {
        "id": "DailyDialog",
        "display_name": "Daily Dialog",
        "task": "dailydialog",
        "tags": ["ChitChat", "Dodeca"],
        "description": (
            "A dataset of chitchat dialogues with strong annotations for "
            "topic, emotion and utterance act. This version contains both sides "
            "of every conversation, and uses the official train/valid/test splits "
            "from the original authors."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1710.03957"},
    },
    {
        "id": "EmpatheticDialogues",
        "display_name": "Empathetic Dialogues",
        "task": "empathetic_dialogues",
        "tags": ["ChitChat", "Dodeca"],
        "description": (
            "A dataset of 25k conversations grounded in emotional situations "
            "to facilitate training and evaluating dialogue systems. "
            "Dataset has been released under the CC BY-NC license."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1811.00207"},
        "notes": (
            "EmpatheticDialoguesTeacher returns examples like so: \n\n"
            "  - [text]:  context line (previous utterance by 'speaker') \n"
            "  - [labels]: label line  (current utterance by 'listener') \n\n"
            "with additional task specific fields: \n\n"
            "  - [situation]: a 1-3 sentence description of the situation that the conversation is \n"
            "  - [emotion]: one of 32 emotion words \n\n"
            "Other optional fields: \n\n"
            "  - [prepend_ctx]: fasttext prediction on context line - or None \n"
            "  - [prepend_cand]: fasttext prediction on label line (candidate) - or None \n"
            "  - [deepmoji_ctx]: vector encoding from deepmoji penultimate layer - or None \n"
            "  - [deepmoji_cand]: vector encoding from deepmoji penultimate layer for label line (candidate) - or None "
        ),
    },
    {
        "id": "DialogueSafety",
        "display_name": "Dialogue Safety",
        "task": "dialogue_safety",
        "tags": [],
        "description": (
            "Several datasets described in the paper Built it Break it Fix it "
            "for Dialogue Safety: Robustness from Adversarial Human Attack. "
            "All datasets are classification tasks in which the goal is to "
            "determine if the text is offensive or 'safe'."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1908.06083"},
    },
    {
        "id": "MultiWOZv2.0",
        "display_name": "MultiWOZ 2.0",
        "task": "multiwoz_v20",
        "tags": ["Goal"],
        "description": (
            "A fully labeled collection of human-written conversations spanning"
            "over multiple domains and topics."
        ),
        "links": {"website": "http://dialogue.mi.eng.cam.ac.uk/index.php/corpus/"},
    },
    {
        "id": "MultiWOZv2.1",
        "display_name": "MultiWOZ 2.1",
        "task": "multiwoz_v21",
        "tags": ["Goal"],
        "description": (
            "A fully labeled collection of human-written conversations spanning"
            "over multiple domains and topics."
        ),
        "links": {"website": "http://dialogue.mi.eng.cam.ac.uk/index.php/corpus/"},
    },
    {
        "id": "SelfChat",
        "display_name": "SelfChat",
        "task": "self_chat",
        "tags": [],
        "description": "Not a dataset, but a generic world for model self-chats.",
    },
    {
        "id": "OneCommon",
        "display_name": "OneCommon",
        "task": "onecommon",
        "tags": ["Goal"],
        "description": (
            "A collaborative referring task which requires advanced skills "
            "of common grounding under continuous and partially-observable context. "
            "This code also includes reference-resolution annotation."
        ),
        "links": {"website": "https://github.com/Alab-NII/onecommon"},
    },
    {
        "id": "IGC",
        "display_name": "Image Grounded Conversations",
        "task": "igc",
        "tags": ["Visual", "ChitChat", "Dodeca"],
        "description": (
            "A dataset of (image, context, question, answer) tuples, comprised "
            "of eventful images taken from Bing, Flickr, and COCO."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/1701.08251"},
    },
    {
        "id": "ANLI",
        "display_name": "Adversarial Natural Language Inference (ANLI) Corpus",
        "task": "anli",
        "tags": ["Entailment", "NLI"],
        "description": (
            "The ANLI corpus (version 1.0) is a new large-scale NLI benchmark dataset,"
            "collected via an iterative, adversarial human-and-model-in-the-loop procedure"
            "with the labels entailment, contradiction, and neutral. A total of three rounds "
            "of data are collected that progressively increase in difficulty and complexity."
        ),
        "links": {
            "github": "https://github.com/facebookresearch/anli",
            "arXiv": "https://arxiv.org/abs/1910.14599",
        },
    },
    {
        "id": "NLI",
        "display_name": "Natural Language Inference (NLI) Corpus",
        "task": "nli",
        "tags": ["Entailment"],
        "description": (
            "A collection of 3 popular Natural Language Inference(NLI) benchmark tasks: "
            "ANLI v0.1, MultiNLI 1.0, SNLI 1.0."
        ),
    },
    {
        "id": "Funpedia",
        "display_name": "Funpedia",
        "task": "funpedia",
        "tags": [],
        "description": (
            "Task for rephrasing sentences from Wikipedia conditioned on a persona."
        ),
    },
    {
        "id": "LIGHTGenderBias",
        "display_name": "LIGHT Gender Bias",
        "task": "light_genderation_bias",
        "tags": [],
        "description": ("Task for debiasing the LIGHT dataset."),
        "links": {"arXiv": "https://arxiv.org/abs/1911.03842"},
    },
    {
        "id": "AirDialogue",
        "display_name": "AirDialogue",
        "task": "airdialogue",
        "tags": ["Goal"],
        "description": (
            "Task for goal-oriented dialogue using airplane booking conversations "
            "between agents and customers."
        ),
        "links": {"website": "https://github.com/google/airdialogue"},
    },
    {
        "id": "HollE",
        "display_name": "Holl-E",
        "task": "holl_e",
        "tags": ["ChitChat"],
        "description": (
            "Sequence of utterances and responses with background knowledge about"
            "movies. From the Holl-E dataset."
        ),
        "links": {"website": "https://github.com/nikitacs16/Holl-E"},
    },
    {
        "id": "ELI5",
        "display_name": "ELI5",
        "task": "eli5",
        "tags": ["QA"],
        "description": (
            "This dataset contains Question and Answer data from Reddit "
            "explainlikeimfive posts and comments."
        ),
        "links": {"website": "https://github.com/facebookresearch/ELI5/"},
    },
    {
        "id": "ReDial",
        "display_name": "ReDial",
        "task": "redial",
        "tags": ["ChitChat", "Goal"],
        "description": (
            "Annotated dataset of dialogues where users recommend movies to each other."
        ),
        "links": {"website": "https://redialdata.github.io/website/"},
    },
    {
        "id": "DREAM",
        "display_name": "DREAM",
        "task": "dream",
        "tags": ["QA"],
        "description": (
            "A multiple-choice answering dataset based on multi-turn, multi-party dialogue."
        ),
        "links": {"website": "https://dataset.org/dream/"},
    },
    {
        "id": "C3",
        "display_name": "C3",
        "task": "c3",
        "tags": ["QA"],
        "description": (
            "A multiple-choice answering dataset in Chinese based on a prior passage."
        ),
        "links": {"website": "https://dataset.org/c3/"},
    },
    {
        "id": "CommonSenseQA",
        "display_name": "CommonSenseQA",
        "task": "commonsenseqa",
        "tags": ["QA"],
        "description": (
            "CommonSenseQA is a multiple-choice Q-A dataset that relies on commonsense "
            "knowlegde to predict correct answers."
        ),
        "links": {"wesite": "https://www.tau-nlp.org/commonsenseqa"},
    },
    {
        "id": "StyleGen",
        "display_name": "Style-Controlled Generation",
        "task": "style_gen",
        "tags": ["ChitChat"],
        "description": (
            "Dialogue datasets (BlendedSkillTalk, ConvAI2, EmpatheticDialogues, and "
            "Wizard of Wikipedia) labeled with personalities taken from the Image-Chat "
            "dataset. Used for the style-controlled generation project"
        ),
    },
    {
        "id": "GoogleSGD",
        "display_name": "GoogleSGD",
        "task": "google_sgd",
        "tags": ["Goal"],
        "description": (
            "The Schema-Guided Dialogue (SGD) dataset consists of over 20k "
            "annotated multi-domain, task-oriented conversations between a "
            "human and a virtual assistant."
        ),
    },
    {
        "id": "TaskMaster2",
        "display_name": "TaskMaster2",
        "task": "taskmaster2",
        "tags": ["Goal"],
        "description": (
            "The second version of TaskMaster, containing Wizard-of-Oz dialogues "
            "for task oriented dialogue in 7 domains."
        ),
    },
    {
        "id": "GenderationBiasControlTask",
        "display_name": "GenderationBiasControlTask",
        "task": "genderation_bias:controllable_task",
        "tags": [],
        "description": (
            "A teacher that wraps other ParlAI tasks and appends control tokens to the "
            "text field indicating the presence of gender words in the label(s)."
        ),
    },
    {
        "id": "MDGender",
        "display_name": "MD Gender",
        "task": "md_gender",
        "tags": [],
        "description": (
            "Tasks for the multi-dimensional gender bias classifier training."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/2005.00614"},
    },
    {
        "id": "Sensitive Topics Evaluation Topics Valid Teacher",
        "display_name": "Sensitive Topics Evaluation Topics Valid Teacher",
        "task": "sensitive_topics_evaluation",
        "tags": [],
        "description": (
            "Task for evaluating a classifier trained to identify conversational messages "
            "on the following sensitive topics: Politics, Drugs, Medical Advice, Religion, "
            "Relationships & Dating / NSFW."
        ),
        "links": {"arXiv": "https://arxiv.org/abs/2010.07079"},
    },
    {
        "id": "decode",
        "display_name": "DialoguE COntradiction DEteCtion (DECODE)",
        "task": "decode",
        "tags": ["ChitChat", "Entailment"],
        "description": "Task for detect whether the last utterance contradicts previous dialogue history.",
        "links": {"arXiv": "https://arxiv.org/abs/2012.13391"},
    },
    {
        "id": "metalwoz",
        "display_name": "MetaLWOz",
        "task": "metalwoz",
        "tags": ["Goal"],
        "description": (
            "Meta-Learning Wizard-of-Oz (MetaLWOz) is a dataset designed to help "
            "develop models capable of predicting user responses in unseen domains."
        ),
        "links": {
            "paper": "http://workshop.colips.org/dstc7/dstc8/DTSC8_multidomain_task_proposal.pdf",
            "website": "https://www.microsoft.com/en-us/research/project/metalwoz/",
        },
    },
    {
        "id": "Wizard_of_Internet",
        "display_name": "Wizard_of_Internet",
        "task": "wizard_of_internet",
        "tags": ["ChitChat"],
        "description": (
            "A dataset with conversations directly grounded with knowledge "
            "retrieved from internet. One of the participants has access to internet search. "
            "The other side has an assigned persona that provides the topic of the conversation. "
            "Contains 93.7k utterances from 9.6k conversations, split into train, "
            "test, and valid sets."
        ),
    },
    {
        "id": "msc",
        "display_name": "MultiSessionChat",
        "task": "msc",
        "tags": ["ChitChat"],
        "description": (
            "A multi-session human-human chit-chat dataset consist of session 2-5 follow up from PersonaChat "
            "It contains 5k full converesations from session 2 to session 5 (session 1 being PersonaChat) "
        ),
    },
    {
        "id": "jericho_world",
        "display_name": "JerichoWorld",
        "task": "jericho_world",
        "tags": [],
        "description": (
            "Jericho World dataset: common sense in a text-based game. "
            "The goal is generating the knowledge graph of the game state "
            "or the set of valid actions from the text descriptions of the world."
        ),
    },
    {
        "id": "CaSiNo",
        "display_name": "CaSiNo (CampSite Negotiation Dialogues)",
        "task": "casino",
        "tags": ["Negotiation"],
        "description": (
            "A dataset of 1030 negotiation dialogues. Two participants take the role of campsite neighbors and negotiate for Food, Water, and Firewood packages, based on their individual preferences and requirements."
        ),
        "links": {
            "paper": "https://aclanthology.org/2021.naacl-main.254.pdf",
            "website": "https://github.com/kushalchawla/CaSiNo",
        },
    },
]
