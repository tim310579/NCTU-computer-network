# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

> TODO: 
> * Describe how to execute your program
   * 先設定好9個switch和6個host，並按照要求在他們之間建立link和設置相關參數，之後設置一個net來模擬送封包的過程，並用dump查看nodes的狀態。
    執行topology.py，並輸入指令 "h4 iperf -s -u -i 1 > ./out/result & "和" h2 iperf -c 10.0.0.4 -u –i 1 "，封包送完後顯示loss為53% 
> * Show the screenshot of using iPerf command in Mininet
   * ![image](https://github.com/nctucn/lab2-tim310579/blob/master/lab2-image.png?raw=true)
---
## Description

### Mininet API in Python

> TODO:
> * Describe the meaning of Mininet API in Python you used in detail
 * 用nodes可以查看節點訊息，然後用link查看每個連結是否正確，然後用net查看整個網路拓樸的狀態
### iPerf Commands

> TODO:
> * Describe the meaning of iPerf command you used in detail
 * iperf主要是用來測試兩節點間的連結，如題目要求用h4和h2來進行測試
### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**
 * 先用學號後五碼登入pietty後，用root和密碼登入，之後將資料夾clone下來，並用mn指令進入mininet的測試

2. **Example of Mininet**
 * 運行看看mininet是否能正常運作，若發生錯誤，打打看mn -c，清除之前的資料後再試一次

3. **Topology Generator**
 * 我的學號是0616027，mod 3 後是1，所以根據topo1.png建立一個網路拓樸，首先建立host和switch，之後建立link並加入相關參數，然後在code中加入dumpNodeConnections(net.hosts) dumpNodeConnections(net.switches) CLI(net)，分別查看host和switch狀態，還有整個net的狀態

4. **Measurement**
 * 根據要求(topo1.png)，iperf h4 和 h2，並得到loss的結果為53%，落在範圍51-58%之間
---
## References

> TODO: 
> * Please add your references in the following
> * [SDN 學習Day2-初探Mininet](https://ithelp.ithome.com.tw/articles/10157657)
* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

> TODO:
> * Please replace "YOUR_NAME" and "YOUR_GITHUB_LINK" into yours

* [Yu-Ming Chen](https://github.com/tim310579)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3
