# Route Configuration

This repository is a lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program with Ryu SDN framework to build a simple software-defined network and compare the different between two forwarding rules.

---
## Objectives

1. Learn how to build a simple software-defined networking with Ryu SDN framework
2. Learn how to add forwarding rule into each OpenFlow switch

---
## Execution

> TODO:
> * How to run your program?
   * 先運行 " mn --custom topo.py --topo topo --link tc --controller remote" 指令，然後再另一台運行" ryu-manager SimpleController.py -–observe-links" 指令，之後在mininet打"mininet> h1 iperf -s -u -i 1 –p 5566 > ./out/result1 & ， mininet> h2 iperf -c 10.0.0.1 -u –i 1 –p 5566"，跑完後會發現最下面有server report，告訴你傳封包的情況及丟包率。(controller.py情況相同)

> * What is the meaning of the executing command (both Mininet and Ryu controller)?
   * 打開topo的mininet，然後再使用controller來控制topo的封包寄送狀況，之後在mininet裡用iperf把h1當server，測出去的流量，在把h2當client，iperf出去的流量，然後將結果顯示出來(interval, transfer, bw,丟包率等)。
> * Show the screenshot of using iPerf command in Mininet (both `SimpleController.py` and `controller.py`)
  * SimpleController
  * ![image](https://github.com/nctucn/lab3-tim310579/blob/master/simplecontroller.png?raw=true)
  * controller
  * ![image](https://github.com/nctucn/lab3-tim310579/blob/master/controller.png?raw=true)
---
## Description

### Tasks

> TODO:
> * Describe how you finish this work in detail

1. Environment Setup
* 登入root，改完密碼後進入src，查看mn指令是否能使用。
2. Example of Ryu SDN
* 測試看看ExampleTopo.py和SimpleController是否可以運行，並出現預期結果。如下圖
![image](https://github.com/nctucn/lab3-tim310579/blob/master/example.png?raw=true)
3. Mininet Topology
* 把SimpleTopo.py的東西複製到topo.py裡面去，之後改一下bw, loss, delay，然後測試topo和SimpleController是否能使用，因為沒注意到助教給的指令有些有錯，所以在這邊多花了點時間，最後也是沒什麼問題。
4. Ryu Controller
* 一樣把SimpleController裡的東西複製到controller裡，然後在裡面新增幾條flow，分別是h2->s3->s2，s3->s2->s1，s2->s1->h1，並把原本的h2->s3->s1和s3->s1->h1刪掉，這樣就完成controller.py了。
5. Measurement
* 測試topo，controller.py是否有錯，在打ryu-manager controller.py -–observe-links 時，一直出現同樣的錯誤，弄了兩三個小時才知道要新增PYTHONPATH到src裡，之後就順利的完成測試，得出如之前的螢幕截圖結果。
### Discussion

> TODO:
> * Answer the following questions

1. Describe the difference between packet-in and packet-out in detail.
* packet-in就是從該switch/host 的哪一條編號阜進去，所以用inport，packet-out就是從該switch/host 的哪一條編號阜出去，用的是actions = [parser.OFPActionOutput("which route out")]。
2. What is “table-miss” in SDN?
* 一個packet在flow table裡沒有能夠匹配的flow entry(不知道要從哪出去)，就是table-miss，可能直接丟掉，或傳給別人處理，或是拿去問remote controller。
3. Why is "`(app_manager.RyuApp)`" adding after the declaration of class in `controller.py`?
* 為了要繼承RyuApp的一些功能，繼承之後有些指令就不用特別宣告即可使用。
4. Explain the following code in `controller.py`.
    ```python
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    ```
* 主要負責管理未知目的地的封包，因此需要管理packet-in事件，
5. What is the meaning of “datapath” in `controller.py`?
* 封包從一處流到另一處中間所經過的路徑，可以想成是一座橋，連接兩端的switch/router。
6. Why need to set "`ip_proto=17`" in the flow entry?
* ip_protocol有很多種協定，17是用於UDP傳送封包時所用的編號。
7. Compare the differences between the iPerf results of `SimpleController.py` and `controller.py` in detail.
* 經過多次測試發現SimpleController.py 的丟包率會高一點，可能是一條路徑同時有多個封包經過，造成丟包率較高，或是沒有設置bw, loss, delay所造成。也有可能是走不同路徑導致丟包率降低。
8. Which forwarding rule is better? Why?
* controller.py，因為丟包率可能比較低。
---
## References

> TODO: 
> * Please add your references in the following
* (https://hk.saowen.com/a/cd9fbf72be915e923b77ab37dcf625f324e5e47e1352d9d5d631285d6edac571)
* (https://gist.github.com/aweimeow/d3662485aa224d298e671853aadb2d0f)
* (https://osrg.github.io/ryu-book/zh_tw/html/openflow_protocol.html?fbclid=IwAR1wzCCVgJGEcGpBXuxyM5ER4hAOT5P2-5426DPZrphb0nKJOtAy6hyjLXo)
* **Ryu SDN**
    * [Ryubook Documentation](https://osrg.github.io/ryu-book/en/html/)
    * [Ryubook [PDF]](https://osrg.github.io/ryu-book/en/Ryubook.pdf)
    * [Ryu 4.30 Documentation](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Ryu Controller Tutorial](http://sdnhub.org/tutorials/ryu/)
    * [OpenFlow 1.3 Switch Specification](https://www.opennetworking.org/wp-content/uploads/2014/10/openflow-spec-v1.3.0.pdf)
    * [Ryubook 說明文件](https://osrg.github.io/ryu-book/zh_tw/html/)
    * [GitHub - Ryu Controller 教學專案](https://github.com/OSE-Lab/Learning-SDN/blob/master/Controller/Ryu/README.md)
    * [Ryu SDN 指南 – Pengfei Ni](https://feisky.gitbooks.io/sdn/sdn/ryu.html)
    * [OpenFlow 通訊協定](https://osrg.github.io/ryu-book/zh_tw/html/openflow_protocol.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

> TODO:
> * Please replace "`YOUR_NAME`" and "`YOUR_GITHUB_LINK`" into yours

* [陳昱銘](https://github.com/tim310579)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3
