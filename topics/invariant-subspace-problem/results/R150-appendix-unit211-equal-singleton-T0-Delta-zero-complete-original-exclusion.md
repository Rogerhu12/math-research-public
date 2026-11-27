# R150 附录：等单点值碰撞中 T0 与 Delta 同时为零的整个原面排除

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 结论与范围

在原 unit211 非零孤立 mean 的 $h=k$ 碰撞图中，
$$
\boxed{T_0=0,\quad\Delta=0}
$$
整个原面为空。证明先由两条原仿射值方程迫使唯一有理基参数
$$
\lambda=\frac13,\qquad u=\frac{125}{123},
$$
再保自由 Gram 参数 $f$，返回同一点的完整原方程。两个单点原 mean 的偶、奇行已经给出非零常数线性组合，直接矛盾。

这里物理 $D=0$。本稿没有借用旧 $D\ne0$ 权图的 $T_0$ 排除，也没有倒置 $\Delta$ 或 $N_f$。互补的 $T_0=0,\Delta\ne0$ 另以新两参数输入继续；其他碰撞权面与普通 ISP 均未关闭。

来源：[等值碰撞原 Gram](R150-appendix-unit211-equal-singleton-values-full-original-Gram-and-Delta-quartic.md)、[完整八原权不变量](R150-appendix-unit211-equal-singleton-invariant-weight-full-original-system.md)、[该碰撞整个等权原支已闭](R150-appendix-unit211-equal-singleton-equal-weight-Delta-zero-and-entire-collision-exclusion.md)。原 $h=k=1$、$S=0$ 及 $\lambda=0$ 等已排原支继续使用其原作用域，未重新登记。

## 1. T0 零面上原 P1 支付 Phi

置
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\xi=B/A,
$$
$$
\ell=A^3/B^2,\quad T=A^2/B,\quad
w=\lambda-1-T,\quad h=k=1+\xi,
$$
$$
Q=1-\rho^2,\quad d=1-Q,\quad
b+c=\ell,\quad bp+cq=u,\quad p=1+\rho,\ q=1-\rho.
$$
原碰撞 moment 给出上述 $\ell,T$。因为 $A,B\ne0$，$\ell$ 为单位。由
$$
T_0=2u-\ell Q-2u^2=0
$$
得到
$$
Q=\frac{2u(1-u)}{\ell},\qquad
\Phi=4u-4+Q=\frac{2(u-1)(2\ell-u)}{\ell}.
\tag{1.1}
$$
原 $Q\ne0$ 同时保证 $u\ne0,1$。

仍用原两条仿射行
$$
P_c+P_f f+bcQ\Phi t=0,\qquad
N_c+N_f f+bcQS\xi t=0.
\tag{1.2}
$$
这里
$$
P_f=T_0(J-Q),\quad P_c=QP_{02}(\ell+T)-G_0T_0,
\quad G_0=\lambda P_{02}-(1-u)T_0.
$$
在本面 $P_f=0$，而
$$
\ell+T=\frac{A^2(A+B)}{B^2}
=\frac{A^2\lambda(2\lambda-1)^2}{B^2}.
\tag{1.3}
$$
右端各因子均为原单位：$\lambda=0$ 已排，$2\lambda-1=0$ 属于已经完整处理的原 $S=0$ 支。故 $P_c=QP_{02}(\ell+T)\ne0$。第一原行立即排除 $\Phi=0$，并合法给出
$$
\boxed{\Phi\ne0,\qquad
t=-\frac{P_{02}(\ell+T)}{bc\Phi}.}
\tag{1.4}
$$
没有在尚未证明的边界求逆；(1.4) 对整个 $T_0=0$ 碰撞面都成立。

## 2. 原 Delta 条件只余 lambda=1/3

记
$$
\eta=\xi+3-2\lambda,\quad
S=2\xi+3-2\lambda,\quad
J=2u(1-u)+\ell Q.
$$
在 (1.1) 上 $J=4u(1-u)=2\ell Q$，所以
$$
N_f=(3-4\lambda)Q+J\xi\eta
=Q\left(3-4\lambda+2\ell\xi\eta\right).
$$
用 $\ell\xi=T,\ \ell\xi^2=A$，括号化成
$$
4\lambda^2-8\lambda+5+2(3-2\lambda)A^2/B.
$$
完整多项式身份
$$
(4\lambda^2-8\lambda+5)B+2(3-2\lambda)A^2
=(3\lambda-1)(2\lambda-1)
$$
遂给
$$
\boxed{N_f=Q\frac{(3\lambda-1)(2\lambda-1)}{B},
\qquad \Delta=\Phi N_f.}
\tag{2.1}
$$
两条全参数身份 (1.3)、(2.1) 的分子展开已由先前实际源逐系数返回。因为 $\Phi,Q,B,2\lambda-1$ 在本图非零，$\Delta=0$ 必给 $\lambda=1/3$。

此时原参数准确为
$$
A=\frac59,\quad B=-\frac{14}{27},\quad
\ell=\frac{125}{196},\quad T=-\frac{25}{42},\quad
\xi=-\frac{14}{15},
$$
$$
S=\frac7{15},\quad\eta=\frac75,\quad
w=-\frac1{14},\quad \ell+T=\frac{25}{588}.
\tag{2.2}
$$

## 3. 同一个原 N(V) 条件迫使 u=125/123

在整个 $T_0=0$ 面，
$$
bc=\frac{u^2(2\ell-1)}{4d},\qquad
P_{02}=uQ(2\ell-1).
\tag{3.1}
$$
代入 (2.2)，得
$$
P_{02}=\frac{27}{98}uQ,\qquad
N_c=\eta(-\lambda P_{02}\xi+Qwu)=\frac{uQ}{50}.
$$
第二原行中 $N_f=0$；再用 (1.4) 和 $S\xi=-98/225$，它准确等价于
$$
\frac{uQ}{50}+\frac{QP_{02}}{54\Phi}
=\frac{uQ}{4900\Phi}(98\Phi+25Q)=0.
\tag{3.2}
$$
各被取消因子已在原图非零。由
$$
Q=\frac{392}{125}u(1-u),\quad
98\Phi+25Q
=\frac{392}{125}(u-1)(125-123u)
$$
和 $u\ne1$，得到唯一值
$$
u=\frac{125}{123},\quad
Q=-\frac{784}{15129},\quad
\Phi=\frac{200}{15129}.
\tag{3.3}
$$
这是原同一点的必要参数，不是分别投影后拼接的两个根。

## 4. 保自由 f 的原 mean 常数矛盾

在 (2.2)–(3.3) 上，$f$ 仍是自由变量，$t$ 仅由 (1.4) 定义。按原未缩放 Gram 恢复
$$
W_1=T_0/2+2uf,\quad
W_2=uT_0+\lambda P_{02}+(V_2+2u^2)f-bcQt,
$$
$$
X=\frac{cq(qW_1-W_2)}{bcQ(q-p)},\quad
Y=\frac{bp(W_2-pW_1)}{bcQ(q-p)},
$$
$$
r=X-ap-ct,\ s=Y-aq-bt,\quad
A_1=2f-2bX-2cY+2bct,\quad a=1-\ell.
$$
四个原 Gram 行是
$$
(0,0,p,q),\ (0,A_1,r,s),\ (p,r,0,t),\ (q,s,t,0).
$$
源按原双点乘法和迹完整重建所有原行，实际返回三个 moment、$E_0,N_0,P_1,N_4(V)$，保两个单点原 N/P 的准确目标。这里没有把独立自由参数 $f$ 预先选定。

两个单点原 mean 互为 $\rho\mapsto-\rho$ 的共轭，写作 $E_B=E_{B,e}+\rho E_{B,o}$、$E_C=E_{B,e}-\rho E_{B,o}$。因两原行都要求为零且 $\rho\ne0$，偶、奇部分都必须为零。实际原返回为
$$
E_{B,e}=\frac{2605898}{4412625}-\frac{4406}{2583}f,\qquad
E_{B,o}=-\frac{29258}{35875}+\frac{50}{21}f.
\tag{4.1}
$$
直接精确有理数运算给
$$
\boxed{
E_{B,e}+\frac{2203}{3075}E_{B,o}
=\frac{32956}{5253125}\ne0.
}
\tag{4.2}
$$
这已排除所有复 $f$，也排除两种实际 $\rho$ 根。

执行源独立以 $E_1,E_{B,e}$ 做完整 QQ 扩展 gcd，并实际乘回 $1$；其两个原行、两个完整标签及常数结果仅 277 字节，全部保存于回执。另六原行也已重建，不需要对已成单位再追加验证门。八原式在 $f$ 中的实际次数依次为 $2,1,1,2,3,2,3,2$。

故唯一原基参数候选不可能是原解，整个 $h=k,T_0=\Delta=0$ 面排除。

## 5. 源、真实失败与成功身份

成功源：[完整原有理候选返回](../notes/2026-11-27-unit211-equal-singleton-T0-Delta-zero-complete-original-rational-return-8542.py)。

- git blob：6aee162135c5c7edace4e78a33a3af8c5eaac5c8。
- SHA-256：402d5ce112bbd862d8eaedc5a2447f058bb097d229c6621d5daf04203108dd97。
- [run 46010648548](https://github.com/Rogerhu12/math-research-public/actions/runs/46010648548)，job 140544983517；inner exit 0，源 0.046597331 秒、驱动 0.120085485 秒，峰值 37448 KiB。
- stdout 2587 字节，SHA-256 4e90c2fe5c53ba05d4f9abb0df74e1199639eca4521981767cb8ec56f29f8e69。
- 实际 pull：2026-11-27 13:51:11 UTC，936a740199284fefb3c14d9fe637919bbbf234bc；根及本题 README 均无差异。
- Python 3.12.14、python-flint 0.9.0、单线程、120 秒/1 GiB。
- [成功小回执](../notes/2026-11-27-unit211-equal-singleton-T0-Delta-zero-complete-exclusion-receipt-8542.json)保全部八原式及实际 QQ 单位标签。

先前源 46c5885 的参数片段装配错误造成 NameError/inner exit 1；只完成两个全参数 lambda 恒等式，没有执行原 Gram。该失败的[准确记录](../notes/2026-11-27-unit211-equal-singleton-T0-Delta-zero-first-assembly-failure-8542.md)保持不变。成功源恢复原参数后继续首次原 Gram 返回，没有把旧失败改写成成功。

下一输入处理 $T_0=0,\Delta\ne0$：利用 (3.1) 及原两行，直接在 $(\lambda,u)$ 上写出未缩放的 $f,t$，再返回全部八式和固定 QQ 投影。这个互补原面在本稿结束时仍开放；本稿不把它的尚未运行输入列为结论。
