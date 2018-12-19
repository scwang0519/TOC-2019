# TOC-2019
chatbot

A Facebook messenger bot based on a finite state machine


## Setup

### Prerequisite
* Python 3
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

#### Secret Data

`VERIFY_TOKEN` and `ACCESS_TOKEN` **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
./ngrok http 5000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
Later to show the pic.

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
        * Input: "go to dogs"
                * Reply: "I'm entering dogs"

        * Input: "go to cats"
                * Reply: "I'm entering cats"   

        * Input: "go to others"
                * Reply: "I'm entering others"

Then, you can input `pictures` to see some cute pictures.
When you are in `dogs`, you can choose three kinds of dogs, `corgi`, `husky`, or `shiba inu` by facebook buttons.
When you are in `cats`, you can choose two kinds of cats, `kitten` or `cat` by facebook buttons.
When you are in `others`, you can choose the `surprise` button to see the surprise animal :D !

When you are in any states but user, input `back` will go to `user`.

## Reference
Class Theory of Computation 2018
Introductions by TAs on moodle
