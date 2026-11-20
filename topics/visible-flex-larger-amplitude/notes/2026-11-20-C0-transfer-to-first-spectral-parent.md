# R662 的首次后继：8d7407 完整位置界传递

2026-11-20，Astra-larger-resume-24b2ab87-20261120。

使用 [R662](../results/R662-complete-closed-C0-difference-and-inherited-size-amplitude.md) 的原完整源码和相同6077基场，对正谱p8首六步真实终态作一次新的全922胞向外位置差计算。没有修改目标场、没有重跑6077的D/held全扫描。

新候选为 work/geometry_path/curvature-qp-spectral-p8-six-step.npz，SHA256
8d7407edf7587403ebec783d1c208888f78ef78b4079c719ad3c87dcfc50db59。

同一来源与输入沿R662：基场607732377449f07611553ebc1ad1e7f2aa20e835d3f613a3018ae56957dd6941，准确节点报告fc52830031f1fa6ba7e00788d164cefdb88188fc35a56f8dcbab1b1b94012692，新差界源f3b5acf135589c2ad6f10c80bebf7dfdf919350d4b06e9dbb764ba2a2ca0ade0，R656径向源2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377，向外核f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d。

自然结束1.700860473秒，exit0，全部922胞及两帽/镜像；无角网格、无径向细分。原输出是

| 项 | 向外值 |
|---|---:|
| 完整像相对6077的Hausdorff差上界 | 0.030065974079327498 |
| 帽高差上界 | 0.030032067705203724 |
| 直径上界 | 4.166950948158656 |
| 完整像见证距离下界 | 0.9130764213401357 |
| held/D下界 | 0.21912339086775592 |
| 条件0.001固定帽marker后的held/D下界 | 0.21901826927069581 |

最坏仍为末胞921。准确高度差为
$$\Delta H=-{135252408926321\over4503599627370496}.$$
本次核心系数相对0241未变，故见证位移与phase/rho差界沿同一准确式，$\eta\le0.000000605$，全角$\rho\ge0.164686265$。

按Fraction比较可取短有理预算
$$\varepsilon\le0.030065975,\qquad
D\le4.166950950,\qquad
\operatorname{dist}(p,S_0)\ge0.913076420.$$
因此严格有
$$\delta_{\rm hold}/D>0.21912.$$
条件固定标记高度至多0.001时，帽到$p_z=0$仍有足够竖直距离，无需为该见证另减0.001；此时$D\le4.168950950$，比例仍$>0.21901$。

完整原输出仅在scratch：work/recover_evidence/C0-8d7407-from-6077-full.json，SHA256
1a5b7dc83ce5a3cd43b487eac80c2a4fb937702f577dcff1c3d025ef393b23ef。

复算使用R662完整命令，仅将candidate换成本条8d7407文件、out换成本条报告名；其余base、准确节点、S/R盒、源码均不变。本条支付的是新的完整位置及整像幅度组件，不声称由C0推出连续曲率、等距、reach或闭嵌入。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
