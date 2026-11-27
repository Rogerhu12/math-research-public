# R150 附录：Q=1−u 边界上 ell=0 整权线的原低度返回

日期：2026-11-27（台北，UTC+8）；会话 Astra-ISP-8542。

## 1. 结论和原输入

在原 unit-(2,1,1) 的一般 LS 系统中，
$$
Q=1-u,\qquad \ell=b+c=0
$$
整条权线没有物理解。这里不需要假设 $u=1/2$，也不使用其异常纤维排除；本稿独立支付一般 $Q=1-u$ 余支中后续参数图所需的 $\ell\ne0$。

沿用原归一化
$$
r^2=u,\quad p=1+r,\quad q=1-r,\quad
b=r/2,\quad c=-r/2,\quad a=1,
$$
$$
X=x+yr,\quad Y=x-yr,\quad Q=1-u.
$$
原物理单位及 $P_{02}\ne0$ 在此给出
$$
u(1-u)(2u-3)\ne0,\qquad bc=-u/4,\qquad
P_{02}=u(u-1)(2u-3).
\tag{1.1}
$$
已发布 $Q=1-u,\ y=1$ 整支排除，允许取 $y\ne1$。

源从 Frobenius 迹
$\tau(v)=v_0+v_1+bv_B+cv_C$ 和原四条 Gram 行重新构建。具体定义与同一 $Q=1-u$ 原模型一致：
$$
f=\frac{x+y-(1-u)}2,\quad
r_G=X-p-ct,\quad s_G=Y-q-bt,
$$
$$
A_1=2f-2bX-2cY+2bct,
$$
$$
k_0=(0,0,p,q),\quad k_1=(0,A_1,r_G,s_G),\quad
k_B=(p,r_G,0,t),\quad k_C=(q,s_G,t,0).
$$
源保留原 E0/N0/P1 对 $\lambda,T$ 的恢复，并直接乘回；不选择独立的 $r$ 嵌入。以下的 $E_1,R_t,R_y,N_H,N_S,P_S$ 全是这些原行或同一原 singleton 值等式的必要加权行。

## 2. 两条原均值方程合法恢复 t 和 x

原 $R_y$ 精确化为
$$
R_y=(y-1)\{u(t+2y)-2x\}+(1-u)(2y-1).
\tag{2.1}
$$
令 $A_y=-R_y|_{t=0},\ B_y=u(y-1)$。对原每行
$J(t)=\sum_{j=0}^dJ_jt^j$，先取完整齐次返回
$$
\widehat J=\sum_{j=0}^dJ_jA_y^jB_y^{d-j}.
\tag{2.2}
$$
这只用了已付 $u(y-1)$，且保留全部原系数。次数
$d(E_1),d(R_t),d(N_H),d(N_S),d(P_S)$ 分别是
$1,2,2,3,3$；源从原次数至多 3 的公式精确恢复并逐项乘回。

令 $v=2y-1$。原 $E_1$ 的 (2.2) 返回恰为
$$
\widehat E_1=u(1-u)
\left\{v^2x+\frac{v^3-(4u+3)v^2-v-1}{4}\right\}.
\tag{2.3}
$$
若 $v=0$，此式等于 $-u(1-u)/4\ne0$，故完整支付 $v\ne0$。
于是原均值方程唯一给出
$$
x=u+\frac34-\frac v4+\frac1{4v}+\frac1{4v^2},
\tag{2.4}
$$
$$
y=\frac{v+1}{2},\qquad
t=\frac{2x}{u}-(v+1)-\frac{2(1-u)v}{u(v-1)}.
\tag{2.5}
$$
这里 $v-1\ne0$ 正是已付 $y\ne1$，没有引入未登记的均值首项单位。

实现中仍不直接丢弃有理分母：写
$\widehat E_1=Lx+C$，其中 $L=u(1-u)(2y-1)^2$，然后对每个原返回
$\widehat J=\sum_{j=0}^nJ_jx^j$ 使用
$$
\mathcal J=\sum_{j=0}^nJ_j(-C)^jL^{n-j}.
\tag{2.6}
$$
只清除、剥除 (1.1) 的原参数单位。记整理后的四条必要行是
$\mathcal R,\mathcal N,\mathcal S,\mathcal P$，分别来自
$R_t,N_H,N_S,P_S$。在 $v$ 坐标中，其 $(v,u)$ 次数是
$$
(8,1),\quad (8,3),\quad(12,7),\quad(12,7).
$$
全部有理常数规范由附源确定；没有使用 $2u-1$ 作为单位。

## 3. 原 Rt 的新低度因式和完整二次纤维

同一原 $\mathcal R$ 精确因式为
$$
\mathcal R=
\frac{(v^2+1)^2}{16}
\left\{4uv^3(2-v)-(v^2+1)^2\right\}.
\tag{3.1}
$$
先返回整个 $v^2+1=0$ 纤维，不能把这个因子直接删除。

在完整商代数 $K=\mathbb Q[v]/(v^2+1)$ 内，同一原 $\mathcal N$ 为
$$
u^2\left\{\frac{3+v}{2}+(v-1)u\right\}.
\tag{3.2}
$$
因为 $u\ne0$，且 $(v-1)(-v-1)=2$ 在 $K$ 内可逆，(3.2) 迫
$u=1/2+v$。此时同一原 $\mathcal S$ 的值是
$$
\mathcal S(1/2+v,v)=\frac{-109+787v}{64}.
\tag{3.3}
$$
它与 $v\mapsto-v$ 的共轭之积为
$$
\frac{315625}{2048}\ne0.
$$
所以 (3.3) 是完整商代数内的单位，对 $v=\pm i$ 两个实际根均不为零。整个纤维排除。

源同时在该完整商代数中对 $\mathcal N,\mathcal S,\mathcal P$ 作扩展 Euclid：
真实 gcd 为 $u^2$，每个系数逆、除法和 Bézout 都乘回，共 7 次逆、5 次除法、2 次 Bézout。这里的显示值 (3.2)–(3.3) 已给出不依赖抽象域嵌入的纸面排除。

## 4. 余支的一元原返回

现已有 $v(v^2+1)\ne0$。由 (3.1)，$v=2$ 会留下非零常数 $-(v^2+1)^2$，故也完整支付 $v\ne2$。于是
$$
u=\frac{(v^2+1)^2}{4v^3(2-v)}=\frac{B(v)}{A(v)}.
\tag{4.1}
$$
对每条 $\mathcal J=\sum_{j=0}^d a_j(v)u^j$ 作完整齐次返回
$$
J^\sharp(v)=\sum_{j=0}^d a_j(v)B(v)^jA(v)^{d-j}.
\tag{4.2}
$$
来自原 $\mathcal N,\mathcal S,\mathcal P$ 的三条完整 QQ 多项式次数分别为
20、40、40。

实际完整 QQ 扩展 Euclid、乘回得到
$$
\gcd(N^\sharp,S^\sharp)
=\gcd(N^\sharp,S^\sharp,P^\sharp)
=v^4(v^2+1)^4.
\tag{4.3}
$$
第一次 Bézout 的两个乘子次数分别是 27、7。源直接检查
$sN^\sharp+tS^\sharp=v^4(v^2+1)^4$ 的所有系数；
没有用模 gcd 猜测 (4.3)。

作为小输入的显式核对，
$$
N^\sharp=-\frac12v^4(v^2+1)^4
\left(6v^8-26v^7+40v^6-27v^5+15v^4-10v^3+2v^2+v+1\right).
$$
因此 (4.3) 的右端只含第 2–3 节已经支付的单位，在任何本支原解处非零，矛盾。至此所有 $u$ 都已覆盖，结论成立。

## 5. 执行证据和未闭范围

自含 JS 源 SHA-256：
$$
\texttt{7c231709422820f0a0ed97ddc33d55053391675d5ac7ae0949d454a490b48d60}.
$$
源共 16,871 个 ASCII 字符，完整从原 Gram 构建到最后 QQ Bézout 已在纯 V8 实际执行成功，用时 2,322 毫秒。只使用 BigInt 的精确有理运算，不依赖 scratch 数据、外部库、数值根或重建猜测。小回执保留源哈希、完整次数、原 Rt 因式、二次纤维值、逆/除法计数和完整 gcd。

这条结论允许一般 $Q=1-u$ 余支使用 $\ell\ne0$，从而进一步考虑同源参数
$$
z=\frac{\ell(u+y-x)-uy}{y-1}.
$$
它不声称已排除 $\ell\ne0,\ H_Q\ne0,\ y\ne1$ 的全部余支，更不声称已完成普通 ISP。
