# R150 补充：W 四条原三次式的实际二元头与两个未付零面

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。

## 1. 输入与完整乘回

本补充记录已刊“四条 S-free 原三次式、原理想相等与二元三次头结式”的 W 实例首次实际计算，不改写其先前通用九系数证书。原 S 一次系统正式提交为
`8c7f1580abcd7df252ea4f8b8f1306ba4b526dfb`。

沿用同一个已付局部环及该文的
$$
G_F=FB_*-B_F,\quad G_\lambda=\lambda B_*-B_\lambda,\quad
G_4=B_*^2-\delta LB_*+\delta^2C.
$$
令 $B_*=aF^2+bF\lambda+c\lambda^2+h_1+c_0$，
$Z=aF+b\lambda,\ Y=c\lambda$。本次实际乘回
$$
G_\times=\lambda G_F-FG_\lambda=FB_\lambda-\lambda B_F,
$$
$$
G_{\rm red}=G_4-ZG_F-YG_\lambda,\qquad
G_4=G_{\rm red}+ZG_F+YG_\lambda.
$$
完整原迹、所有已付单位归一化比例、反向身份与几何次数上界均实际核验。没有新除 $\delta$、几何变量或二次头系数。

实际 $G_\times$ 为 1383 项，权双次数 $(14,16)$、几何总次数 3，标准字符串 SHA256：
`fe28d4e5d85d5068c16d2006e0c430f4df5b20faa4acf0a6289cdda5ae183544`。
$G_{\rm red}$ 为 4598 项，权双次数 $(24,29)$、几何总次数 3，SHA256：
`4d0bcfd7fc6603b708d02113cadf97a5f796389d8d38f1c61e1334c144778ac2`。

## 2. 完整头因子与适用范围

按列 $(F^3,F^2\lambda,F\lambda^2,\lambda^3)$ 取四条实际归一化原三次式的头，得到 $H_{\rm actual}$。其行列式双次数为 $(53,72)$。依序剥已付参数 gcd，非平凡循环计数为
$$
k:2,\quad u:2,\quad V:11,\quad
\operatorname{num}(P_{02}):4,\quad
\operatorname{num}(bc):3,\quad
\operatorname{num}(\ell):2,\quad
\operatorname{num}(\ell-u):1.
$$
这些次数是源码的实际 gcd 循环次数，不将整个已付多项式擅自解释为相应幂。记各次实际 gcd 的乘积为 $\Pi_{\rm head}$；每次 exact division 及最终乘积都乘回。完整剩余因式分解是
$$
\det H_{\rm actual}
=-2^{21}\Pi_{\rm head}D_{27}^{\,2}B_{239}.
$$
其中 $D_{27}$ 与原 S 一次系统的同一 27 项因子相同，双次数 $(5,6)$、总次数 9、SHA256：
`171698e50a84a1bb7bf4c4f6f7d6514f48d10a39b86cc4f85c3c7f6c7b2b2b09`。
$B_{239}$ 为 239 项，双次数 $(15,22)$、总次数 28，SHA256：
`2e704c7b1bcc53e94bd378b8302351bea6ce67ac6245b4c4a603f7e023cb08b5`。
其精确系数由自含公开源的原四头行列式、逐次已付剥除与完整因式分解定义和再生，无大系数缓存。完整因子乘回已经实际成功，不遗漏其他头零因子。

因此 $D_{27}B_{239}\ne0$ 是合法后续二元六生成元图。这里尚未计算该图的显式头逆；$D_{27}=0$ 与 $B_{239}=0$ 两整面均未支付。本次也尚未将原 $N_s/P_s$ 在同一个恢复的 S 上消去，不声称整个有限原系统排空。

## 3. 唯一实际运行回执

自含源：
`notes/2026-11-27-unit211-generic-LS-W-four-S-free-original-cubics-and-binary-head-8542.py`，
Git blob `d015fb9c74d80e01ee648edd819b11838659bc12`，
18167 字节，SHA256：
`00c08b48852bc8c38041a617d616922c94b6ab0e6f66c393a7e679949b44568e`。

Actions run 45972117428 / job 140414825063；180 秒、4 GiB 界限。源耗时 7.452089667 秒，驱动 7.548856299 秒，最大子进程 RSS 90736 KiB，退出码 0。stdout 14443 字节，SHA256：
`497e90c741965ba3f07a183ccc400a335c4d257bc72fb17e8ebc772c352f3874`。

实际 pull 为 2026-11-27 09:15:11.690463 UTC，前后同提交
`8fa535aed5ae04e39b05a705868f761df7935d83`。
根 README blob `282e86b03385d3b6245ce7100ae2e2af7b103c2d`，
课题 README blob `5fbd905291dd044c88d35bd9c07ac0e586ff795a`，均无变化。

本次是新的四三次头输入的首次实际构建；没有重跑已冻结参数 cofactor 或 Gröbner 门。
