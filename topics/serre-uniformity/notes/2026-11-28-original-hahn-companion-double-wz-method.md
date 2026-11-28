# 原 Hahn companion 双和的精确双变量 telescoper：有限公开请求

日期：2026-11-28。状态：**方法及证书框架已纸证；脚本未运行，尚无 telescoper 回执**。
数学只在本公开仓库 GitHub Actions 运行。本文不含素数扫描、数值拟合或原 $e,K_4$ 非同时零断言。

## 1. 固定原输入，保持 literal-$N$ lift

来源为 R1194 的 (HC.19)–(HC.21)、(HC.30)、(HA.1)。
对每个整数 $N\ge0$，在 $\mathbb Q$ 中定义
$$
u_r=\frac{(2/3)_r(1/6)_r(1/2)_r}{(4/3)_r(r!)^2},
$$
$$
W_N=\sum_{\substack{r,s\ge0\\r+s\le N}}
u_r\frac{(-N+r)_s\,s!\,(2/3)_s}
{(r+4/3)_s(3/2)_s(5/3)_s}.
\tag{DW.1}
$$
这里的 $-N+r$ 按所写的整数参数保留；不先用 $N=-5/6$ 替换，也不换成另一个较容易的 characteristic-zero lift。

在真正的原源 $p=6N+5\ge41$ 下，(HC.21) 逐项给
$$
w(-1/2)=-\frac K{12}W_N\pmod p.
\tag{DW.2}
$$
$K$ 是 (HC.19)/(HA.22) 的同一单位。
所有输入分母都是 $p$ 单位：$r+s\le N$，所以 $(r+4/3)_s$ 的三倍因子至多 $3N+1$，
$(3/2)_s$ 的两倍因子至多 $2N+1$，$(5/3)_s$ 的三倍因子至多 $3N+2$；
原 $u_r$ 的分母同样安全。
因此这是原 companion 的一个精确、有理数值可定义的 lift。

区别必须保留：若直接在特征零用 (HC.20) 的同一有理系数向下求逆、取尾 $t_{N+1}=0$，
会得到另一个 lift $S_N$。它容易纸证
$$
S_n-(1+\rho_n)S_{n-1}+\rho_nS_{n-2}
=-\frac{u_n}{36(n+1/3)(n+1/6)},\qquad
\rho_n=\frac{(n-2/3)(n-1/6)(n-1/3)}
{(n+1/3)^2(n+1/6)}.
$$
这在原特征只给 $S_{N+1}-S_N=4u_N/9$，重现既付旁强迫。
本请求不以它替换 (DW.1)。

## 2. 保全部边界的坐标改变

令新坐标 $s,t\ge0$、$r=N-s-t$，则 (DW.1) 等于
$$
W_N=\sum_{\substack{s,t\ge0\\s+t\le N}}F_N(s,t),
$$
$$
F_N(s,t)=
\frac{(-1)^s(2/3)_r(1/6)_r(1/2)_r
(s+t)!\,s!\,(2/3)_s}
{(4/3)_{N-t}(r!)^2\,t!\,(3/2)_s(5/3)_s}.
\tag{DW.3}
$$
其来源就是 $(-s-t)_s=(-1)^s(s+t)!/t!$。
在整数格上将 $r<0$ 的值定义为零，这与 reciprocal factorial $(r!)^{-2}$ 的双零一致；
所有其他相关 Gamma/Pochhammer 参数都是非整数，不在这个边界引入反向极。
不能在原 $(r,s)$ 三角形上直接延长较低 $N$ 的那一行，因为原有理式在 $r>N$ 不自动为零；
(DW.3) 正是避免这一漏洞的实际坐标。

固定求解阶 $\tau\ge1$，置 $M=N+\tau$、$r=M-s-t$、$\ell=M-t$，
并令 $\alpha$ 遍历 $2/3,1/6,1/2$。写
$$
Q_j(r)=\prod_\alpha(r+\alpha-j)_j,\qquad
D_\tau(r)=\prod_\alpha(r+\alpha-\tau).
$$
从公共最高行 $F_M$ 降 $d$ 步的准确比为
$$
C_d=
\frac{(r-d+1)_d^2(\ell+4/3-d)_d}
{\prod_\alpha(r+\alpha-d)_d},
\qquad 0\le d\le\tau.
\tag{DW.4}
$$
当 $0\le r<d$，分子含真正零因子，故这仍给被截掉行的零。
因此可以将所有 $W_{N+j}$ 同时放在公共三角形 $s+t\le M$ 中，而不增加虚假端项。

## 3. 两个实际 forward ratios 和证书框架

公共项的两个比为
$$
\frac{F_M(s+1,t)}{F_M(s,t)}
=-\frac{r^2(s+t+1)(s+1)(s+2/3)}
{\prod_\alpha(r+\alpha-1)(s+3/2)(s+5/3)},
$$
$$
\frac{F_M(s,t+1)}{F_M(s,t)}
=\frac{r^2(s+t+1)(\ell+1/3)}
{(t+1)\prod_\alpha(r+\alpha-1)}.
\tag{DW.5}
$$
对待求 $P_s,P_t\in\mathbb Q(N)[s,t]$，取
$$
G_s=\frac{s(s+1/2)(s+2/3)P_s}{Q_{\tau-1}(r)}F_M,\qquad
G_t=\frac{tP_t}{Q_{\tau-1}(r)}F_M.
\tag{DW.6}
$$
所有 $Q_j(r)$ 在整数 $r$ 上均无零。
$s=0$、$t=0$ 两条下边分别被显式因子杀掉；
外斜边 $r=-1$ 被 reciprocal factorial 双零杀掉，并没有未处理的 $0$ 乘极。
由
$$
Q_\tau(r)=\prod_\alpha(r+\alpha-1)\,Q_{\tau-1}(r-1)
=D_\tau(r)Q_{\tau-1}(r)
$$
可知所求恒等证书恰是以下 $\mathbb Q(N)[s,t]$ 多项式等式：
$$
\begin{aligned}
&-(s+t+1)(s+1)^2(s+2/3)r^2P_s(s+1,t)\\
&\quad-D_\tau(r)s(s+1/2)(s+2/3)P_s(s,t)\\
&\quad+(s+t+1)(\ell+1/3)r^2P_t(s,t+1)
-D_\tau(r)tP_t(s,t)\\
&=\sum_{j=0}^{\tau}a_j(N)\,
 (r-\tau+j+1)_{\tau-j}^{\,2}
 (\ell+4/3-\tau+j)_{\tau-j}
 \prod_\alpha\prod_{h=\tau-j+1}^{\tau}(r+\alpha-h).
\end{aligned}
\tag{DW.7}
$$
右端每列就是 $C_{\tau-j}Q_\tau$，总次数均为 $3\tau$。

若 (DW.7) 找到且 $a_\tau\ne0$，先除 $Q_\tau$，再对公共三角形求和，全部边界严格为零，
于是
$$
\boxed{\sum_{j=0}^{\tau}a_j(N)W_{N+j}=0.}
\tag{DW.8}
$$
脚本将整个证书向量一次清 $\mathbb Q(N)$ 分母及整系数 content，
故 raw 版本对所有 $N\ge0$ 成立。
若再去掉递推各系数的公共多项式因子，则只在该公共因子不为零的特征零整数处直接使用；
输出必须保留公共因子及其全部非负整数零点，不能丢掉这些例外。

## 4. 有限算法和预算

请求固定 $\tau=1,2,3,4$，依次尝试
$$
\deg_{s,t}P_s\le3\tau+1,\qquad
\deg_{s,t}P_t\le3\tau+3.
$$
这是声明的有限 ansatz，不声称涵盖所有可能证书，也不依据任何采样值选择参数。
将 (DW.7) 各单项式系数排列为 $\mathbb Q(N)$ 矩阵，
求完整右核，只接受最后一个 shift 系数非零的核向量。
最大一层为 $210$ 行、$246$ 列；其中自然可能包含纯 curl 证书，
所以不能把核非零本身当成找到递推。

统一墙钟预算为 $3600$ 秒，保留 $90$ 秒给回执；
进程内 alarm 在 $3510$ 秒触发，外层 Docker 再有有限硬超时。
固定官方 SageMath 10.6 镜像与既有本仓库 symbolic WZ 工作流相同。
不安装新包，不调用网络数学服务，不写回仓库，不生成 artifact 或 Release 数据。

若四层均未找到非零末 shift，或有限预算耗尽，只报告这个有限 ansatz 未成功；
不能报告不存在 telescoper，也不能报告原 $w$ 或 $K_4$ 的任何非零结论。

## 5. 验证与输出

找到候选后，脚本必须完成：

1. 在 $\mathbb Q(N)[s,t]$ 中完整展开 (DW.7)，验证余式严格为零。
2. 独立用 (DW.5) 和 (DW.6) 重建两个 rational forward differences，
   在分式域中再次验证 $\Delta_sG_s+\Delta_tG_t=\sum a_jC_{\tau-j}F_M$。
3. 一次清全证书的分母、polynomial gcd 和整数 content，保持所有证书和递推的同一尺度。
4. **只有在 exact 证书已得之后**，对固定 $N=0,1,2,3,5$ 及其所需 shifts，
   用 (DW.1) 和 (DW.3) 两个完整有理和互核，并检查完整递推。
   这些是转录/边界审计，既不拟合递推，也不是素数窗口。
5. 输出小型完整证书、规范 JSON 的 SHA-256、Sage 版本、source/request/method/README pins、
   run/commit 标识与实际耗时。可重算输出不提交入库。
6. 对 primitive 递推各系数，读取它含因子 $6N+5$ 的精确重数，
   并输出在 $N=-5/6$ 的准确有理值。此步是符号特化，不选任何素数。

这里的 symbolic recurrence 只为下一步原窗口的消元提供可核输入。
即便递推存在，$W_{N+j}$ 对 $j\ne0$ 与原 $e,K_4$ 的来源比较仍须另付；
不因 (DW.8) 或某个系数单位，就宣称原双零已排除。

## 6. 已有静态检查范围

O1 全文推导了 (DW.3)–(DW.8) 及支撑。
O2 已独立纸核两份 forward ratio、$C_d$、清分母四项与三条边界，
并静态读完脚本的 Sage/API、两份 exact residual、清分母及 primitive gcd 例外处理；
没有执行或编译数学脚本，也没有把静态审核称作实际运行成功。

