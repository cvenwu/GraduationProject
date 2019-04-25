# GraduationProject
毕业设计 基于CNN和词向量的句子相似性度量

##  环境

1. 

## 参考资料

1. [文本相似度比对](https://blog.csdn.net/diye2008/article/details/53762124?ref=myread)

2. 老师给的链接：  [文本相似度比对](https://blog.csdn.net/Mr_carry/article/details/80996454)

3. [link](https://blog.csdn.net/xiangz_csdn/article/details/54580053)

4. 余弦距离计算公式：

![余弦距离计算公式](D:/git%E4%BB%93%E5%BA%93/DiplomaProject/%E4%BD%99%E5%BC%A6%E8%B7%9D%E7%A6%BB.jpg)



<details>
<summary>展开查看</summary>
<pre><code>.
├── Owner: maojian,haoguanwei
├── app
│   ├── Owner: maojian,haoguanwei,linmiao
│   ├── admin
│   │   ├── ep
│   │   │   ├── merlin
│   │   │   │   └── Owner: maojian,yuanmin,fengyifeng,xuneng
│   │   ├── main
│   │   │   ├── activity
│   │   │   │   └── Owner: liweijia,zhapuyu,renwei
│   │   │   ├── answer
│   │   │   │   └── Owner: zhaogangtao
│   │   │   ├── search
│   │   │   │   └── Owner: liweijia,zhapuyu,renwei,guanhuaxin
│   │   │   ├── sms
│   │   │   │   └── Owner: renwei,zhapuyu
│   │   │   ├── spy
│   │   │   │   └── Owner: zhaogangtao
│   │   │   ├── tag
│   │   │   │   └── Owner: renwei,renyashun
│   │   │   ├── tv
│   │   │   │   └── Owner: liweijia,renwei
│   │   │   ├── up
│   │   │   │   └── Owner: shencen,wangzhe01
│   │   │   ├── upload
│   │   │   │   └── Owner: haoguanwei,zhapuyu
│   │   │   ├── usersuit
│   │   │   │   └── Owner: zhaogangtao
│   │   │   ├── videoup
│   │   │   │   └── Owner: shencen,wangzhe01
│   │   │   ├── videoup-task
│   │   │   │   └── Owner: shencen,wangzhe01
│   │   │   ├── vip
│   │   │   │   └── Owner: zhaogangtao
│   │   │   └── workflow
│   │   │       └── Owner: haoguanwei,zhapuyu,zhuangzhewei,zhoushuguang
│   │   └── openplatform
│   │       └── sug
│   │           └── Owner: changxuanran,xucheng
│   ├── common
│   │   └── openplatform
│   │       └── Owner: liuzhan,huangshancheng
│   ├── interface
│   │   ├── live
│   │   │   ├── Owner: liuzhen
│   │   │   └── push-live
│   │   │       └── Owner: kuangxibin
│   │   └── main
│   │       ├── account
│   │       │   └── Owner: wanghuan01,zhoujiahui,zhaogangtao,chenjianrong,zhoujixiang
│   │       ├── activity
│   │       │   └── Owner: liweijia
│   │       ├── answer
│   │       │   └── Owner: zhaogangtao
│   │       ├── app-channel
│   │       │   └── Owner: peiyifei
│   │       ├── app-feed
│   │       │   └── Owner: peiyifei
│   │       ├── app-interface
│   │       │   └── Owner: peiyifei
│   │       ├── app-player
│   │       │   └── Owner: peiyifei
│   │       ├── app-resource
│   │       │   └── Owner: peiyifei
│   │       ├── app-show
│   │       │   └── Owner: peiyifei
│   │       ├── app-tag
│   │       │   └── Owner: peiyifei
│   │       ├── app-view
│   │       │   └── Owner: peiyifei
│   │       ├── app-wall
│   │       │   └── Owner: peiyifei
│   │       ├── article
│   │       │   └── Owner: changxuanran,lijiadong,qiuliang
│   │       ├── broadcast
│   │       │   └── Owner: chenzhihui,caoguoliang,guhao
│   │       ├── captcha
│   │       │   └── Owner: chenzhihui
│   │       ├── creative
│   │       │   └── Owner: shencen,wangzhe01
│   │       ├── credit
│   │       │   └── Owner: zhaogangtao
│   │       ├── dm
│   │       │   └── Owner: liangkai,renwei
│   │       ├── dm2
│   │       │   └── Owner: liangkai,renwei
│   │       ├── esports
│   │       │   └── Owner: liweijia,zhapuyu
│   │       ├── favorite
│   │       │   └── Owner: chenzhihui,lujinhui
│   │       ├── feedback
│   │       │   └── Owner: peiyifei
│   │       ├── growup
│   │       │   └── Owner: gaopeng
│   │       ├── history
│   │       │   └── Owner: renwei,wangxu01
│   │       ├── kvo
│   │       │   └── Owner: liweijia,zhapuyu
│   │       ├── laser
│   │       │   └── Owner: haoguanwei,shencen
│   │       ├── player
│   │       │   └── Owner: liweijia,zhapuyu
│   │       ├── playlist
│   │       │   └── Owner: liweijia
│   │       ├── push
│   │       │   └── Owner: renwei,zhapuyu
│   │       ├── push-archive
│   │       │   └── Owner: zhapuyu,shencen,renwei,liweijia,wangzhe01
│   │       ├── reply
│   │       │   └── Owner: lujinhui,chenzhihui,caoguoliang
│   │       ├── report-click
│   │       │   └── Owner: zhangshengchao,chenzhihui,renyashun
│   │       ├── shorturl
│   │       │   └── Owner: peiyifei,zhapuyu
│   │       ├── space
│   │       │   └── Owner: liweijia,zhapuyu
│   │       ├── spread
│   │       │   └── Owner: zhapuyu,renwei
│   │       ├── tag
│   │       │   └── Owner: renwei,renyashun
│   │       ├── tv
│   │       │   └── Owner: renwei,liweijia
│   │       ├── upload
│   │       │   └── Owner: peiyifei,zhapuyu
│   │       ├── videoup
│   │       │   └── Owner: shencen,wangzhe01
│   │       ├── web
│   │       │   └── Owner: liweijia,zhapuyu
│   │       ├── web-feed
│   │       │   └── Owner: zhapuyu,liweijia,renwei
│   │       ├── web-goblin
│   │       │   └── Owner: liweijia,renwei
│   │       └── web-show
│   │           └── Owner: liweijia
│   ├── job
│   │   ├── live
│   │   │   ├── Owner: liuzhen
│   │   │   └── wallet
│   │   │       └── Owner: lixiang,zhouzhichao
│   │   ├── main
│   │   │   ├── account-notify
│   │   │   │   └── Owner: wanghuan01
│   │   │   ├── account-summary
│   │   │   │   └── Owner: zhoujiahui
│   │   │   ├── history
│   │   │   │   └── Owner: renwei,wangxu01
│   │   │   ├── identify
│   │   │   │   └── Owner: linmiao,wanghuan01
│   │   │   ├── member
│   │   │   │   └── Owner: chenjianrong,zhoujiahui,linmiao,zhoujixiang
│   │   │   ├── passport
│   │   │   │   └── Owner: wanghuan01
│   │   │   ├── passport-auth
│   │   │   │   └── Owner: wanghuan01
│   │   │   ├── passport-encrypt
│   │   │   ├── reply
│   │   │   │   └── Owner: chenzhihui,lujinhui,caoguoliang
│   │   │   ├── search
│   │   │   │   └── Owner: liweijia,zhapuyu,renwei,guanhuaxin
│   │   │   ├── sms
│   │   │   │   └── Owner: renwei,zhapuyu
│   │   │   ├── spy
│   │   │   │   └── Owner: zhaogangtao
│   │   │   └── workflow
│   │   │       └── Owner: haoguanwei,zhapuyu
│   │   └── openplatform
│   │       └── open-market
│   │           └── Owner: changxuanran,liuyan02,qiuliang
│   ├── service
│   │   ├── ep
│   │   │   └── saga-agent
│   │   │       └── Owner: muyang,tangyongqiang,fangrongchang
│   │   ├── live
│   │   │   ├── Owner: liuzhen
│   │   │   ├── userexp
│   │   │   │   └── Owner: kuangxibing
│   │   │   └── wallet
│   │   │       └── Owner: lixiang,zhouzhichao
│   │   ├── main
│   │   │   ├── account
│   │   │   │   └── Owner: wanghuan01,zhoujiahui
│   │   │   ├── antispam
│   │   │   │   └── Owner: chenzhihui,lujinhui
│   │   │   ├── archive
│   │   │   │   └── Owner: haoguanwei,peiyifei
│   │   │   ├── assist
│   │   │   │   └── Owner: shencen,wangzhe01
│   │   │   ├── block
│   │   │   │   └── Owner: zhaogangtao
│   │   │   ├── favorite
│   │   │   │   └── Owner: chenzhihui,lujinhui
│   │   │   ├── feed
│   │   │   │   └── Owner: renwei,zhapuyu
│   │   │   ├── figure
│   │   │   │   └── Owner: zhaogangtao
│   │   │   ├── filter
│   │   │   │   └── Owner: zhaogangtao,muyang
│   │   │   ├── identify
│   │   │   │   └── Owner: wanghuan01
│   │   │   ├── identify-game
│   │   │   │   └── Owner: wanghuan01
│   │   │   ├── location
│   │   │   │   └── Owner: peiyifei,haoguanwei
│   │   │   ├── member
│   │   │   │   └── Owner: zhaogangtao,wanghuan01,zhoujiahui,chenjianrong,zhoujixiang
│   │   │   ├── msm
│   │   │   │   └── Owner: maojian
│   │   │   ├── notify
│   │   │   │   └── Owner: haoguanwei,lintanghui
│   │   │   ├── passport
│   │   │   │   └── Owner: wanghuan01
│   │   │   ├── search
│   │   │   │   └── Owner: liweijia,zhapuyu,renwei,guanhuaxin
│   │   │   ├── secure
│   │   │   │   └── Owner: zhaogangtao,lintanghui
│   │   │   ├── seq-server
│   │   │   │   └── Owner: peiyifei
│   │   │   ├── share
│   │   │   │   └── Owner: peiyifei,haoguanwei
│   │   │   ├── sms
│   │   │   │   └── Owner: renwei,zhapuyu
│   │   │   ├── spy
│   │   │   │   └── Owner: zhaogangtao
│   │   │   ├── tag
│   │   │   │   └── Owner: renwei,renyashun
│   │   │   ├── thumbup
│   │   │   │   └── Owner: liweijia,zhapuyu,renwei
│   │   │   ├── up
│   │   │   │   └── Owner: shencen,wangzhe01
│   │   │   ├── upcredit
│   │   │   │   └── Owner: shencen,wangzhe01
│   │   │   ├── usersuit
│   │   │   │   └── Owner: zhaogangtao
│   │   │   ├── videoup
│   │   │   │   └── Owner: shencen,wangzhe01
│   │   │   ├── vip
│   │   │   │   └── Owner: lintanghui,zhaogangtao
│   │   │   └── workflow
│   │   │       └── Owner: haoguanwei,zhapuyu,zhoushuguang
│   │   └── openplatform
│   │       ├── abtest
│   │       │   └── Owner: lijiadong,qiuliang
│   │       ├── anti-fraud
│   │       │   └── Owner: wanglitao,wangminda,jiayanxiang
│   │       ├── ticket-item
│   │       │   └── Owner: yangyucheng
│   │       └── ticket-sales
│   │           └── Owner: liuzhan,yangyucheng
│   └── tool
│       ├── cache
│       │   └── Owner: zhapuyu
│       ├── ci
│       │   └── Owner: tangyongqiang
│       ├── creater
│       │   └── Owner: chenjianrong
│       ├── gdoc
│       │   └── Owner: lintanghui
│       ├── saga
│       │   └── Owner: muyang,tangyongqiang
│       └── warden
│           └── Owner: weicheng
└── library
    ├── cache
    │   ├── memcache
    │   │   └── Owner: maojian
    │   └── redis
    │       └── Owner: maojian
    ├── container
    │   └── pool
    │       └── Owner: zhapuyu
    ├── database
    │   ├── elastic
    │   │   └── Owner: haoguanwei,renwei,zhapuyu
    │   └── sql
    │       └── Owner: 
    ├── ecode
    │   ├── Owner: all
    │   └── tip
    │       └── Owner: all
    ├── exp
    │   └── feature
    │       └── Owner: zhoujiahui
    ├── log
    │   └── Owner: maojian
    ├── naming
    │   └── discovery
    │
    │   │       │   │   └── Owner: 
    │   │       │   ├── rate
    │   │       │   │   └── Owner: 
    │   │       │   ├── supervisor
    │   │       │   │   └── Owner: 
    │   │       │   ├── tag
    │   │       │   │   └── Owner: maojian
    │   │       │   └── verify
    │   │       │       └── Owner: maojian,zhoujiahui
    │   │       └── render
    │   │           └── Owner: 
    │   ├── metadata
    │   │   └── Owner: 
    │   ├── netutil
    │   │   └── breaker
    │   │       └── Owner: 
    │   ├── rpc
    │   │   └── warden
    │   │       ├── Owner: maojian,caoguoliang
    │   │       ├── balancer
    │   │       │   └── wrr
    │   │       │       └── Owner: caoguoliang
    │   │       └── resolver
    │   │           └── Owner: caoguoliang
    │   └── trace
    │       └── Owner: maojian
    ├── rate
    │   └── limit
    │       └── bench
    │           └── stress
    │               └── Owner: lintanghui
    ├── stat
    │   └── sys
    │       └── cpu
    │           └── Owner: caoguoliang
    └── sync
        └── errgroup
            └── Owner: 
</code></pre>
</details>

