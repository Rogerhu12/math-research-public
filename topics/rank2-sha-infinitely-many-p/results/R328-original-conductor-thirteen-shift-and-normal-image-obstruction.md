# R328：原导子的十三行运输与真正的归一化像障碍

日期：2026-11-13。**状态：全部已证明。首40次导子给一个 primitive 原来源嵌入；完整目标增加十三行后，其全部 Smith 成本准确为两个各十三行的跨界带。第一次提升的剩余商明确为目标除以归一化像及这二十六条边界，而非来源的归一化商。没有遗漏目标高行，也没有把导子或新单位判为中央零。**

## 1. 同一原导子、同一物理轴

采用 R322、R326 的
$$A=7bS(z),\quad B=7bS(\delta z),\quad C=7bS(2z),
\qquad b=17,\quad\deg(A,B,C)=(1,3,4).$$
令 $R=\mathbf Z[1/(42b)]$，原加权环与归一化分别为 $\mathcal T_R,\mathcal N_R$。
记 $t=-b/x^3$、$a=t(t-1)h_7$、$h_7=16t^2+4t+7$。
R326 的首导子是
$$
G_0=\frac{A^{40}N(t)}{T_{40}(t)},\qquad
T_{40}=t^{30}(t-1)^{26}(1+8t)^{20}h_7^{30},
\tag{1}
$$
其中 $N\in\mathbf Z[t]$ primitive，$\deg N=147$，
$$N(t)=3^4\,7^3\,3159421\,t^3+O(t^4).$$
全部原40次代表和全次数返回已经由 R326 及 R322 支付：
$$\boxed{G_0\mathcal N_{R,n}\subset\mathcal T_{R,n+40}\quad(n\ge0).}\tag{2}$$

置 $w=z^6$。因
$$\frac{a^{40}}{T_{40}}
=\frac{t^{10}(t-1)^{14}h_7^{10}}{(1+8t)^{20}},$$
故实际首系数为
$$
\boxed{G_0=c_*w^{13}+O(w^{14}),\qquad
c_*=-3^4\,7^{13}\,3159421\,b^{13}.}
\tag{3}
$$
固定整数3159421为素数且模6余1，证书给出完整有限试除。因此对本篇惰性
$p=6s-1>7,p\ne17$，$c_*$ 自动为单位；没有新惰性坏素数。
在一般好特征中则还应明确排除3159421。

取 $s>13$，并设
$$L=2s+\ell,\qquad0\le\ell,\qquad\ell+13<s.\tag{4}$$
所有物理轴只用到长度 $L+13<3s$，仍在 R309、R322 已付的整数范围内。
沿用 $\kappa=34c_p$、$a_p=p\kappa\in\mathcal O^\times$、
$g=e^{-\kappa w^s}\rho$、$t=t(w)$。
定义所需长度内的确切整单位
$$
u_*(w)=\frac{a(t(w))^{40}N(t(w))}
 {c_*w^{13}T_{40}(t(w))}\pmod{w^L},\qquad u_*(0)=1.
$$
它的计算只需已付的 $t(w)$ 至次数 $L$。取该多项式在较长目标中的整提升；
高于等于 $L$ 的任何选择在再乘 $w^{13}$ 后均消失。
则在长度 $L+13$ 的原目标中
$$
\boxed{\mathcal J(G_0)=c_*w^{13}\mathcal U,\qquad
\mathcal U=g^{40}u_*\,e_2(40a_p\epsilon)\in\Gamma_{L+13}^{\times}.}
\tag{5}
$$
这是同一个、与输入列无关的目标单位。真实 charge40、原高轴整系数及
$a_p$ 的全部位都在 (5) 中，没有按列另选 gauge。

## 2. 完整十三行运输：没有丢弃末行

记 $\Lambda_M$ 为长度 $M$ 的原加权前缀格，其基为
$$e_r=w^r/p^{\lfloor r/s\rfloor},\qquad0\le r<M.$$
这只是表示 $\Gamma_M$ 整基的方便记号，不是在整数环中任意除以 $p$。
普通物理级数先乘 $w^{13}$ 给一个整数线性映射
$$m_{13}:\Lambda_L\longrightarrow\Lambda_{L+13}.$$
它不是把截断环 $\Gamma_L$ 免费嵌入较长截断环，而是先乘到足够阶后再截断。
准确地，
$$
\boxed{m_{13}(e_r)=p^{\Delta_r}e_{r+13},\qquad
\Delta_r=\left\lfloor\frac{r+13}{s}\right\rfloor
 -\left\lfloor\frac r s\right\rfloor.}
\tag{6}
$$
由 (4)，$\Delta_r$ 只取0、1，等于1的输入行准确是
$$
\boxed{s-13\le r<s,\qquad2s-13\le r<2s.}
\tag{7}
$$
两带都完整保留到输出中：第二带到达原第三块的最初十三行；
输出第三块的长度为 $\ell+13$，正好包含这些行。总指数准确为26。

对任意 $P\in\mathcal N_{\le D}$，有完整等式
$$
\boxed{\mathcal J_{L+13}(G_0P)
=c_*\mathcal U\,m_{13}(\mathcal J_L(P)).}
\tag{8}
$$
证明可在分式域中的普通有限级数验证：$G_0$ 的阶为13，故 $P$ 的
$w^L$ 以上部分乘后全部落在 $w^{L+13}$ 以上；其余部分用 (5)、(6) 即得。
因此没有把未知的高十三行删去再宣称提升。

## 3. primitive 原嵌入及全部精度的 Smith 比较

**定理1。** 乘 $G_0$ 给出 primitive 嵌入
$$\boxed{G_0:\mathcal N_{\mathcal O,\le D}
\hookrightarrow\mathcal T_{\mathcal O,\le D+40}.}\tag{9}$$
对任意 $N\ge1$，定义有限映射 $J:V\to W$ 的核长度
$$K_N(J)=\operatorname{length}_{\mathcal O}
\ker(V/p^NV\longrightarrow W/p^NW).$$
等价地，它是全部来源 Smith 指数的 $\min(N,\cdot)$ 之和，真实零方向按
$\min(N,\infty)=N$ 计入。则
$$
\boxed{0\le K_N(\mathcal J_{L+13}|_{G_0\mathcal N_{\le D}})
-K_N(\mathcal J_L|_{\mathcal N_{\le D}})\le26.}
\tag{10}
$$
并有
$$K_N(\mathcal J_{L+13}|_{\mathcal T_{\le D+40}})
\ge K_N(\mathcal J_L|_{\mathcal N_{\le D}}).\tag{11}$$

**证明。** (2) 给整数包含。R322 证明每个好剩余域中的归一化是域，且
原幂格向它单射。$G_0$ 模 $p$ 非零，故乘 $G_0$ 在归一化的每个有限分次格
模 $p$ 单射。于是 (9) 的余核无 $p$-挠，有限自由来源的嵌入 primitive。

(8) 的共同单位不改变 Smith；(6) 在特征零上单射且总指数为26。
把目标逐行乘 $p$ 时，任一精度的核长度增加0或1；对 (7) 的二十六行依次
应用即得 (10)。由于 (9) primitive，模每个 $p^N$ 的限制来源仍单射，
其核嵌入原完整来源的核，得到 (11)。$\square$

特别，归一化中任意深度的 primitive 关系只需**一次**固定次数40乘子就
能返回原格。不能在每一层都重收40次成本，也不能把 (10) 的二十六行算成
无界深度收益。原归一化累计维数为 $47D^2/24+O(D)$，固定40次来源开销及
十三行物理开销均已明确保留。

## 4. 下一位究竟要在哪个商中消失

这是比单独知道 (2) 更强、也更有限的实际消障准则。
在剩余目标中记
$$
\mathcal B_{13}=\ker(\bar m_{13})
=\operatorname{span}_k\{w^{s-13+j},\epsilon w^{s-13+j}:0\le j<13\}.
\tag{12}
$$
该空间恰为26维。它的每个方向在整数运输中付一个准确的 $p$，并未被截掉。
设
$$I_{N,D}=\bar{\mathcal J}_L(\mathcal N_{\mathcal O,\le D}/p).$$
定义实际剩余商
$$
\boxed{\mathfrak C_{D,L}^{(13)}
=(\Gamma_L/p)/(I_{N,D}+\mathcal B_{13}).}
\tag{13}
$$

**定理2（原一次提升的准确条件）。** 设 $r\ge1$、
$P\in\mathcal N_{\mathcal O,\le D}$ primitive，且
$\mathcal J_L(P)\in p^r\Gamma_L$。令
$$o_r(P)=p^{-r}\mathcal J_L(P)\bmod p.$$
存在 $Q\in\mathcal N_{\mathcal O,\le D}$ 使
$$
G_0(P-p^rQ)\in\mathcal T_{\mathcal O,\le D+40},\qquad
\mathcal J_{L+13}(G_0(P-p^rQ))\in p^{r+1}\Gamma_{L+13}
\tag{14}
$$
当且仅当
$$\boxed{[o_r(P)]=0\quad\text{在 }\mathfrak C_{D,L}^{(13)}\text{ 中}.}\tag{15}$$
一旦存在，(14) 的原来源仍 primitive。

**证明。** 由 (8)，除以 $p^r$ 后再模 $p$，(14) 的目标像准确等于
$$\bar c_*\bar{\mathcal U}\,ar m_{13}
\bigl(o_r(P)-\bar{\mathcal J}_L(\bar Q)\bigr).$$
前两个因子为单位。因此它为零当且仅当括号落在 (12)，等价于 (15)。
来源成员性由 (2) 给出；模 $p$ 的来源是 $\bar G_0\bar P$，在剩余域的
归一化中非零，故 primitive。$\square$

更换 $P$ 的 $p^r$ 提升只改变 $o_r(P)$ 一个实际归一化像，所以 (15) 是
准确的提升类，不依赖这种选择。对原 $P\in\mathcal T_{\le D}$，R322 的
三块公式 (19) 给出了 $r=1$ 时此类的全部真实系数，包括高轴与首 carry。

若该类本来已落在 $I_{N,D}$，导子当然足够；(12) 再允许二十六个确切边界
方向。其余 $\mathfrak C_{D,L}^{(13)}$ 分量仍是**目标除以真实有限像**的障碍，
来源导子或 $\mathcal N/\mathcal T$ 的有限呈示均不自动消掉它。

## 5. 剩余商的完全明确有限矩阵

使用 R322 的
$$u_n=\lfloor3n/4\rfloor,\quad v_n=\lfloor n/2\rfloor,
\quad c_n=\lfloor2n/3\rfloor,\quad d_n=3u_n+2v_n+c_n,$$
归一化的实际整基是
$$E_{n,j}=A^nt^j/T_n,\qquad0\le n\le D,\quad0\le j\le d_n.$$
其真实径向轴为
$$
H_{n,j}(w)=g(w)^n\frac{a(t(w))^nt(w)^j}{T_n(t(w))}.
\tag{16}
$$
模 $p$ 后，(13) 的像矩阵可以准确用以下列给出：
$$
\boxed{\begin{pmatrix}
[H_{n,j}]_{<s-13}\\
[a_p nH_{n,j}]_{<s-13}\\
[a_p^2n^2H_{n,j}/2]_{<\ell}
\end{pmatrix}.}
\tag{17}
$$
因此 (15) 是 (17) 对应的一个指定非齐次线性系统，不需再解47次隐式关系。
右端分别取真实 $o_r(P)$ 的同一三个前缀；其余二十六行正是 (12)。
这些行的删去是已付的一个 $p$ 运输，而非将完整中央行逐权置零。

在本次模 $p$ 系统中可用 $q=x^{-3}$ 读取同一前缀，将 $g$ 换成 R322
的真实低轴 $\varrho(q)$。但右端 $o_r(P)$ 的计算必须继续使用物理
$w^s=q^s h_0(-bq)^{p+1}$ 及完整三整数块；不能用首次核的换参消去下一位。

## 6. 整个导子中的三条实际连续 charge 方向

R329 的整个导子还给一个方便的明确接口。置
$$v_0(t)=(t-1)(1+8t)h_7(t),\qquad V=A/t=-7x^3S.$$
$V$ 是原椭圆曲线上的全纯 degree34 截面，$V(0)=-7$，因为原 $S$ 在
$O$ 的六阶零恰支付 $x^3$ 的六阶极。它不是新加权环 $\mathcal T$ 的一次元素。
定义
$$
\boxed{K_0=v_0G_0,\qquad K_1=VK_0,\qquad K_2=V^2K_0.}
\tag{18}
$$
则
$$K_i\in(\mathcal T_R:\mathcal N_R)_{40+i},\qquad
\operatorname{ord}_wK_i=13\quad(i=0,1,2).\tag{19}$$

**证明。** R325 的残数记号下，$G_0$ 对应 $dt/Q(t)$，其中
$Q=t(t-1)(1+8t)h_7$。所以 (18) 分别对应
$dt/t,dt/t^2,dt/t^3$，放在典范次数1、2、3。它们在 $0$ 的极阶分别为
1、2、3，不超过 $\lceil3m/4\rceil$；在无穷处也满足允许范围；其他点
无极。因此它们确为有理导子。

相对于 R322(10) 的整数归一化，三个分子准确为
$$
\begin{aligned}
K_0:&\quad N v_0,\\
K_1:&\quad N v_0(t-1)/t,\\
K_2:&\quad N v_0(t-1)^2(1+8t)h_7/t.
\end{aligned}
\tag{20}
$$
它们都是整数多项式，次数分别151、151、155，不超过相应 $d_{40},d_{41},d_{42}$。
R322 的全次数饱和遂使这三条有理导子成为原整数导子；无须新增5、13坏素数。
(3) 及 $v_0(0)=-7,V(0)=-7$ 给 (19)。$\square$

其目标比准确为
$$\mathcal J(K_i)=\mathcal J(K_0)
\bigl(g(w)(t(w)-1)h_7(t(w))e_2(a_p\epsilon)\bigr)^i.
\tag{21}$$
所有 charge 都在式中。可以在原联合像中使用这些已付乘子，不能因此免费
把 $V$ 的全部幂或其完整中央观察加入来源。

同样，若仅重复同一个 $G_0$，在仍处于三块范围的次数 $h$ 内，物理移位
为 $13h$，来源成本为 $40h$，对角因子为
$p^{\lfloor(r+13h)/s\rfloor-\lfloor r/s\rfloor}$。当 $13h<s$ 时每行最多只
增加一层；这条单独的乘法不产生免费的 $c\log D$ 深度。新的净收益仍须
来自 (17) 的真实像包含或不同已付原列的联合取消。

## 7. 完整中央与后续精度的边界

原 $S,S(\delta z),S(2z)$ 的完整中央零仍只按 R314、R319、R322 的准确
尺度等式使用。本文没有给 $G_0P$、$K_iP$ 或 $V$ 新增中央零。

尤其 R324 的强迫项在物理 $w^{5s-1}$。乘 $G_0$ 后它落在 $w^{5s+12}$，
已经越过该五块前缀；不能因五块截断中看不见它，就把它计为已被消去。
若要使用该行，必须支付包含 $w^{5s+12}$ 的更长真实轴和新进位。

本篇已把“付导子以后还缺什么”缩成实际有限商 (13) 与完全明确的矩阵
(17)。证明原完整失败对这个指定剩余类施加的额外约束，才可能给新的深
Smith 输入；来源饱和、余子式矩阵和物理行移各自已经单独付清。

## 固定证书

- `scripts/check-jzero-conductor-thirteen-shift.py/.json`：核原导子首项、固定素因子、同一指数单位、三个 canonical 导子分子及精确跨界运输。

依赖：R322 原饱和与三块下一障碍；R325 典范导子；R326 首五个完整整乘子；
R329 全部十四元导子；R324 第五块原强迫行。
