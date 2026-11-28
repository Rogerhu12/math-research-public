# R150：正确 h=k、Delta=0 原图的固定十七阶覆盖与 5640 个规范点上界

> **后续范围更新（2026-11-28）：** [完整 Pf 静审](../notes/2026-11-28-unit211-h-equals-k-Pf-true-original-static-audit-8542.md)现已支付整个碰撞图的 Pf，因此本页正确覆盖适用于整个当前 Delta 零图。三个小因子的独立原排除进一步将本页5640界收紧为[4788个规范点](R150-appendix-unit211-h-equals-k-corrected-small-factor-exclusions-and-4788-points.md)，仍未排空。下文保留本次运行时的原范围说明。

日期：2026-11-28（Asia/Taipei）。
会话：Astra-ISP-8542378f-20261127。

## 1. 结论及准确范围

本篇只在对称归一的原值碰撞图 $h_U=k_U$ 上工作，保留
$$
ABQ(1-Q)P_f\,bcP_{02}\ne0,\qquad \Delta=0,                 \tag{1}
$$
以及本课题已经独立支付的原物理条件。这里
$$
A=2\lambda^2-2\lambda+1,\qquad
B=4\lambda^3-6\lambda^2+3\lambda-1.
$$
$P_f=0$ 互补支不在本篇范围内；本篇也不使用另一个 W 图的 $D\ne0$ 单位。

正确两条原必要曲线的一个新固定十七阶行列式，实际给出非零
$\mathbb Q[\lambda]$ 多项式，次数为 $716$。只剥去已付的纯 $\lambda$
支持后，保留次数 $470$，完整有理数因式分解为
$$
R_{\rm rem}=\kappa\,C_1^{19}C_2^{14}C_4^6F_{99}F_{300},
\qquad \kappa\in\mathbb Q^\times,                         \tag{2}
$$
其中
$$
\begin{aligned}
C_1&=3\lambda-1,\\
C_2&=3\lambda^2-3\lambda+1,\\
C_4&=8\lambda^4-24\lambda^3+24\lambda^2-12\lambda+3,
\end{aligned}                                           \tag{3}
$$
$F_{99},F_{300}$ 分别为本次完整因式分解中次数 $99,300$ 的不可约
$\mathbb Q$ 因子。它们的准确再生定义和参数 SHA 见第 6 节，
不保存可重算大系数载荷。

因此当前原图的不同 $\lambda$ 至多 $406$ 个。
进一步保留结式的消失重数，而不把平方自由次数误作基点数，得到
$$
\#\{(\lambda,u)\}_{\rm physical}\le470.                    \tag{4}
$$
结合已经发表的完整 $Q$ 与 Loww 纤维论证，得到
$$
\begin{array}{c|c}
\text{不同原坐标点} & \text{上界}\\ \hline
(\lambda,u)&470\\
(\lambda,u,Q)&940\\
(\lambda,u,Q,z),\quad z=Qt&2820\\
\text{完整有序规范原坐标}&5640 .
\end{array}                                             \tag{5}
$$
这些是不同点的上界，不是本篇新证明的全原商长度界。
所有未付谱因子、参数首项零面和每个候选的全部原条件均保留；
本篇不宣称当前碰撞图排空。

## 2. 正确原输入与再生边界

沿已发表的
[正确 Delta=0 的 722 基点覆盖](R150-appendix-unit211-h-equals-k-corrected-Delta-zero-722-base-cover.md)，
使用两条已证原必要曲线
$$
P(\lambda,u)=0,\qquad M_{\rm true}(\lambda,u)=0,\qquad
\deg_{\lambda,u}P=(28,3),\quad
\deg_{\lambda,u}M_{\rm true}=(110,14).                    \tag{6}
$$
先行证明已经实际付清
$\gcd_{\mathbb Q[\lambda,u]}(P,M_{\rm true})=1$。
这排除共同曲线；此处并不把多元 gcd 为一当作无共同点。

独立 $P$ 只来自原 $\Delta,T_n$ 相容式，其规范参数 SHA256 为
8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c，
实际原来源是 run46025096446/job140594347573。
本次仅在 Actions 终端临时读取历史 ac40c96b... 中这一准确输入，
不解码、不使用、不恢复旧错误的第二条曲线；历史文件名中的
“848” 也不是本篇采用的结论。

$M_{\rm true}$ 来源为正确 R/W/O 与原相容式的新输入，
run46120122225/job140902587651，双变量参数 SHA256 为
65d420e901bd60b711d76ad23699daab655414b0595383a19a93d13180f30663。
其源码
[正确 RWO 的 Q 投影定义](../notes/2026-11-28-unit211-h-equals-k-corrected-Delta-zero-RWO-Q-projection-8542.py)
只取到读取旧独立 $P$ 之前的必要定义前缀，精确为 $6055$ 字节、
SHA256 09e0b44a9b6f244d0e2a11c1361b5382219aa5cad609efc3ae08fd370d318c7b。
该前缀内部只用正确 f33 的 $5121$ 字节原 R/W/O 定义。

本次必要系数再生实际核对了 (6) 的两个 SHA。
没有重算先行 P/M 的 QQ gcd、722 计数、旧独立 $\Delta/T_n$ 投影，
也没有执行已经冻结的两个 $z$ 结式目标。
这些前缀只提供新行列式的输入，不另记一个数学结论。

## 3. 固定十七阶原行列式及所有首项退化

分别乘非零有理常数，把 (6) 改成整系数本原多项式
$\widehat P,\widehat M$。本次实际逐系数核回这两个常数缩放。

按 $1,u,\ldots,u^{16}$ 排列列，取前十四行
$u^j\widehat P$，$0\le j<14$，后三行
$u^j\widehat M$，$0\le j<3$，得到固定矩阵
$$
S(\lambda)\in\operatorname{Mat}_{17}(\mathbb Q[\lambda]),
\qquad R_{17}(\lambda)=\det S(\lambda).                  \tag{7}
$$
它与原 $\operatorname{Res}_u(P,M_{\rm true})$ 只差非零有理常数。

若 $(\lambda_0,u_0)$ 是共同有限点，那么
$$
S(\lambda_0)(1,u_0,\ldots,u_0^{16})^t=0.                 \tag{8}
$$
故 $R_{17}(\lambda_0)=0$。这个必要性使用整个固定矩阵，
没有倒置任何 $u$ 首项。专门化后 $u$ 次数下降、
一条曲线在该 $\lambda$ 上成为零多项式、两个首项同为零，
都仍受 (8) 覆盖。

本次用 Bareiss 计算这一个固定行列式，全部 $1496$ 个消去商
逐项验证“商乘除数等于原分子”，没有行交换。
这些是 $\mathbb Q[\lambda]$ 中的多项式恒等式，所以临时主元的
零点不删除任何原纤维。实际行列式非零，次数 $716$；
输入给出的先验上界 $28\cdot14+110\cdot3=722$ 也被满足。

只从 (7) 剥去下列已经独立支付的谱支持：
$$
A,\quad B,\quad\lambda,\quad2\lambda-1,\quad
S_{\rm num}=(2\lambda-1)(2\lambda^2-1),\qquad
S=S_{\rm num}/A.                                       \tag{9}
$$
$A,B$ 为当前原值坐标图单位；$\lambda$ 来自原非零 mean 的
U-value atlas；$2\lambda-1$ 来自独立 347c 原物理排除；
$S$ 来自已逐源码静核的原 S0 碰撞排除。
没有借用错误 compact 均值链，也没有支付一个新的谱首项。

每次 gcd 剥除都保留并乘回其实际因子，给出
$$
R_{17}=U_{\rm paid}\,c\,R_{\rm rem},\qquad
c\in\mathbb Q^\times.                                  \tag{10}
$$
$R_{\rm rem}$ 规范为首一，次数 $470$。
日志中 $A,B,\lambda,2\lambda-1$ 的 gcd 层数分别为
$89,18,5,15$；它们是实际算法层数，尤其不能把
“$B$ 的十八层 gcd”简写成未经核定的 $B^{18}$。
准确数学对象始终是 (10) 实际乘回的 $U_{\rm paid}$。

随后完整 QQ 因式乘积实际返回 $R_{\rm rem}$，
得到 (2)。其平方自由乘积次数是
$$
1+2+4+99+300=406.                                      \tag{11}
$$

## 4. 为何次数 470 控制所有不同 (lambda,u) 点

这里只重用已刊 722 证明中的局部行列式论证，并代入本次实际次数。

固定一个物理 $\lambda_0$，设共有 $r$ 个不同有限共同根
$u_1,\ldots,u_r$。两输入不可能同时在 $\lambda_0$ 上成为零多项式：
否则 $\lambda-\lambda_0$ 在 $\mathbb C[\lambda,u]$ 中整除两者，
与 (6) 已付的无共同曲线矛盾。

因此 $r$ 有限，且 $r\le14<17$。
(8) 给出 $r$ 个线性无关的 Vandermonde 核列，故
$$
\operatorname{nullity}S(\lambda_0)\ge r.                 \tag{12}
$$
在离散赋值环 $\mathbb C[\lambda]_{(\lambda-\lambda_0)}$
上作 Smith 化简，矩阵专门化每少一个秩，行列式至少多一个
$\lambda-\lambda_0$ 因子。因此
$$
\operatorname{ord}_{\lambda_0}R_{17}
\ge \operatorname{nullity}S(\lambda_0)\ge r.             \tag{13}
$$
物理 $\lambda_0$ 上 (9) 的每个支持都非零，所以 (10) 保证
$$
\operatorname{ord}_{\lambda_0}R_{17}
=\operatorname{ord}_{\lambda_0}R_{\rm rem}.               \tag{14}
$$
将 (13) 对全部物理谱值求和，得到 (4)。
此处保留了 (2) 的 $19,14,6$ 重数，
没有错误地用平方自由次数 $406$ 代替全部基点数。

## 5. 完整原纤维恢复与 5640 上界

[Delta 的完整 Q 纤维定理](R150-appendix-unit211-h-equals-k-Delta-zero-complete-Q-fibers-1444-cover.md)
已证明每个允许的 $(\lambda,u)$ 下，原 $\Delta(Q)$
不是恒零多项式，且次数至多二。
它完整处理了三个 $Q$ 系数同时为零的可能性，故不要求一个
新 $Q$ 首项非零。于是每个基点至多给两个 $Q$。

[Loww 完整纤维定理](R150-appendix-unit211-h-equals-k-Delta-zero-complete-Loww-fibers-8664-cover.md)
又给出以下不倒新首项的原必要式。令 $z=Qt$；
在 $P_f\ne0$ 图上，$f,V,x,y,A_1$ 都是 $z$ 的仿射函数。
完整原 Loww 在该纤维上为
$$
L_w(z)=2P_{02}(2\lambda-1)w
 -bc\,t\{K_w+4(f-u)(t-2)\},\qquad \deg_zL_w\le3.         \tag{15}
$$
由原矩参数
$$
w=\lambda-1-\frac{A^2}{B}
=-\frac{\lambda^2(2\lambda-1)}B
$$
可知其常数项
$$
L_w(0)=-\frac{2P_{02}\lambda^2(2\lambda-1)^2}{B}         \tag{16}
$$
是原已付单位。因此每个 $(\lambda,u,Q)$ 的不同 $z$ 至多三个，
包括所有 $z$ 首项退化。

最后 $\rho^2=1-Q$ 至多给两个符号。
给定 $(\lambda,u,Q,z,\rho)$，$t=z/Q$，原 $P_1$ 唯一恢复
$$
f=-\frac{P_c+bc\,\Phi z}{P_f}.
$$
原线性均值唯一恢复 $X,Y,A_1,r,s$；值参数
$\ell=A^3/B^2$、$T=A^2/B$、
$w=\lambda-1-T$、$h_U=k_U=1+B/A$
也都确定。这是固定有序规范图的完整恢复，
没有留下额外自由的 Gram 参数。
于是 $470\cdot2\cdot3\cdot2=5640$，得到 (5)。

这里的“完整”指该规范图内所有原解的必要坐标覆盖；
候选还必须满足同一点的全部原 N/P/Gram 条件。
它不把必要曲线系统说成充分系统，也不计算未经规范化的自由轨道。

## 6. 精确再生定义、参数摘要与首次实际回执

新源：
[固定十七阶原覆盖](../notes/2026-11-28-unit211-h-equals-k-corrected-fixed-u-seventeen-lambda-cover-8542.py)；
原输入说明：
[十七阶输入](../notes/2026-11-28-unit211-h-equals-k-corrected-fixed-u-seventeen-lambda-cover-8542-input.md)。

源 git blob a12ac66b99fb8bc239cd303259c21a705dd02fab，
10330 字节，SHA256
4a8f1140c851838930c7b3992ff318ddda2b1f9ec8da90f08d46bd614749cd25。

| 实际参数定义 | 次数 | 规范字节数 | SHA256 |
| --- | ---: | ---: | --- |
| 固定 $\det S$ |716|155438|0d8d4b94832c4ae4cfab823dd16c6b361e62028010d780e4ee3767826a45aeb7|
| 首一 $R_{\rm rem}$ |470|98375|bb12a30297f6e3e40cd6bc3c06eddc1f653164e8cd80a3fbd22dec017cf665e6|
| 本次 QQ 因子 $F_{99}$ |99|3069|e422b38e5f712eb9237d85ad116dfcdf8ec94f3886a7d97d210b48e3ce6a5a7e|
| 本次 QQ 因子 $F_{300}$ |300|26690|5bfbc9ddc3b558dbef77fc19cd495175a1c8ad16461e6166c44cb982a1dca7ea|
| 平方自由必要乘积 |406|68518|2993b72bd08c047be8fc98f68589856bf94d969629d39a2caf86e4a91ff3af07|

$F_{99},F_{300}$ 的定义就是该固定源中，对 (10) 的首一剩余
多项式作完整 QQ factor 后相应次数的因子；它们各只有一个。
源实际验证全部因子及重数乘回，两个因子的字节规范与源一致。
(3) 三个小因子的升序系数 SHA 分别为
1fa1f30d60b5195a920cd9a68370231ccdd314c1cf5245eb80f5bb78541a427e、
76c6537baea2267477ffc856f1865cc27d5c76cab43f750c63a88cbbdccbf3ab、
c14fdb1890f27b1190806fa0896a5ba77917ef0a5802802eb5b9f65d067aaf26。
小参数识别只对 (3) 的准确系数列表核 SHA，没有重跑结式。

唯一首次 run46124405008/job140915684956：
内层退出 $0$，驱动墙钟 $3.066182153$ 秒，
峰值 RSS $69464$ KiB；
全部 $1779$ 个输入系数缩放、$1623$ 个精确除法乘积
（其中 Bareiss $1496$ 个）、$127$ 个已付支持乘积，
以及完整 QQ 因子乘积均完成。
stdout 为 $7651$ 字节，SHA256
b87cf6a4a2a543f13b916f9582880056d3ef1a9530ae171ea5e64d3f58598f9e。

固定源提交 ce00b012b6db58ea4b1c8125a005efe078cdce96。
真实 git pull 于 2026-11-28 08:08:45.285621 UTC
到 2ece92b92b5775dcbb7bfe17f32ad9e92ee52a41；
根 README 与课题 README 均无变。
小回执：
[实际执行与范围](../notes/2026-11-28-unit211-h-equals-k-corrected-fixed-u-seventeen-lambda-cover-receipt-8542.json)。

没有保存大系数缓存、编码载荷或分片。
本次的新结论是 (2)、(4)、(5)；原 $P_f=0$ 支及所有尚未原返的
谱纤维继续保留。
