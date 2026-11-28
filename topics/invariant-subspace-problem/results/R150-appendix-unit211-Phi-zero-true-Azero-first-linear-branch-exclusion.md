# R150 补充：正确 Phi 的 A=0 上第一条原线性支完整排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 1. 原范围与新分支

保持正确原 unit211 的非零孤立均值图、全部均值和 N/P 值及 jet，并保持
$$
\Phi=0,\qquad Q(1-Q)P_fP_{02}bcD\ne0,\qquad \lambda\ne0.
$$
整 $t=0$ 已由[正确原排除](R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)支付。本条只处理新的正确首项曲线
$$
A=4(u-1)^2-Q=0.
\tag{1}
$$
令
$$
s=u-1,\quad r=u-2,\quad b_0=2u-1,\quad h=2u-3,\quad
\xi=\frac{ut}{2b_0}.
$$
原 Phi 和 (1) 给
$$
Q=4s^2,\quad \ell=\frac{u}{2s},\quad
1-Q=-hb_0,\quad bc=\frac{u^2}{4sb_0},
$$
$$
T_0=-4us,\quad P_{02}=4us^2,\quad P_f=16us^3.
\tag{2}
$$
因此 $u,s,b_0,h$ 以及 $\xi$ 都在本图非零。这些都来自 (2) 与已经完成的整 $t=0$ 排除，不借用被撤回的旧 first-head 单位。

原 $E_0/N_0/P_1$ 精确给
$$
V=bX+cY=u(1-\lambda)+bc\,t,\qquad
f=\frac u2-u\lambda-sT.
\tag{3}
$$
设 $\eta=f-u$。更正后的原紧凑均值在此整曲线上严格因式分解为
$$
\frac{\overline R_{\rm true}}{Q^2}
=(\xi-2\eta)(\xi+2\eta+2u\lambda).
\tag{4}
$$
这给两条完整原线性支。本条证明第一支
$$
\boxed{f=u+\xi/2}
\tag{5}
$$
没有任何原物理点。第二支 $f=u-u\lambda-\xi/2$ 继续保留，不由本条宣布整 $A=0$ 空。

必须区分 (4) 的原来源：在 $E_0=0$ 上，
$$
2\overline R_{\rm true}+Q^2\{E_1-(bE_B+cE_C)\}=0.
$$
因此 (4) 不是单独的 $E_1$ 恒等于零；它与两个 singleton 均值合用才回到完整原均值系统。

## 2. 同一真实 Gram 的完整恢复

在 (5) 上，
$$
T=-\frac{u(2\lambda+1)+\xi}{2s},\qquad
t=\frac{2b_0\xi}{u},\qquad A_1=\xi+2u\lambda.
\tag{6}
$$
形式二次代数同时保留 $\rho^2=1-Q=-hb_0$ 的两个根。设
$$
p=1+\rho,\quad q=1-\rho,\quad
b=\frac{u}{4s}\left(1-\frac{\rho}{b_0}\right),\quad
c=\frac{u}{4s}\left(1+\frac{\rho}{b_0}\right),
$$
$$
x=u+\xi-s\lambda,\qquad y=\frac{r-s\lambda}{h},\qquad
X=x+y\rho,\quad Y=x-y\rho.
\tag{7}
$$
再令
$$
a_w=1-\ell,\quad r_G=X-a_wp-ct,\quad s_G=Y-a_wq-bt.
$$
原四行是
$$
(0,0,p,q),\quad(0,A_1,r_G,s_G),\quad
(p,r_G,0,t),\quad(q,s_G,t,0).
\tag{8}
$$
全过程采用真正 dual 乘法。源码完整返回 $F_2=2f$、原 $E_0/N_0/P_1$、(4) 所需的原 $E_1-E_W$，以及两个 singleton 的共轭关系。没有以一个根的数值替换整个二次代数。

写 $E_B=E_{\rm e}+\rho E_{\rm o}$。新的完整原身份为
$$
E_{\rm e}-b_0E_{\rm o}
=\frac{8s^2}{h}(\lambda+1)(\xi+u\lambda).
\tag{9}
$$
因两个原 singleton 均值都为零，(9) 保留地分成
$$
\lambda=-1\quad\hbox{或}\quad \xi=-u\lambda.
\tag{10}
$$
没有把任一因子作全图单位。

## 3. 小原多项式

从原 $E_{\rm o}$ 和原极化 $N_1-4\lambda wP_{02}$，只移去 (2) 的单位及非零有理常数后，得到
$$
\begin{aligned}
E={}&u(2-u)+2u(2-u^2)\lambda+2u(1-u)\xi
+h\xi^2\\
&+2u(u-2)\lambda\xi-4us^2\lambda^2,
\\
N={}&-sr+(4u^2-11u+8)\lambda-2h\lambda\xi
+(-11u^2+22u-8)\lambda^2.
\end{aligned}
\tag{11}
$$
这是原必要多项式的单位倍数，不是从同解集猜出的替代行。

同样从完整原 weighted N 值条件
$$
bN_4(g_B)+cN_4(g_C)-2\lambda P_{02}(\ell+2T+A_2)=0
$$
得到必要多项式 $S(u,\lambda,\xi)=0$，其紧凑完整定义是
$$
\begin{aligned}
S={}&hr\xi^3-4sh(3u+s\lambda)\xi^2\\
&+u\{32-74u+49u^2-10u^3
 +8s^2(u-4)\lambda-4s^2(3u-2)\lambda^2\}\xi\\
&-2u^4h-4us^2h(3u-2)\lambda
 +16us^2hb_0\lambda^2-16us^3h\lambda^3.
\end{aligned}
\tag{12}
$$
源码也返回原 weighted P 行；以下两个终端分支只需 (11)、(12)。全部原除法都有完整乘回。

## 4. 第一整支：lambda=-1

直接代入 (11)，严格有
$$
N(u,-1,\xi)=2h\{\xi-(4u-3)\},
$$
$$
E(u,-1,\xi)=h(\xi^2-2u\xi-ur).
\tag{13}
$$
由于 $h\ne0$，得 $\xi=4u-3$。第二式继而给
$$
h\,s(7u-9)=0.
$$
只有 $u=9/7,\ \xi=15/7$ 尚可能。完整原 (12) 在该点为
$$
S(9/7,-1,15/7)=\frac{93636}{16807}\ne0.
\tag{14}
$$
因此该整支排空。这里未在得到有限候选后省略原值返回。

## 5. 第二整支：xi=-u lambda

令
$$
E_0=r(1+2\lambda)+(4u^2-9u+4)\lambda^2.
$$
由 (11) 精确有
$$
E(u,\lambda,-u\lambda)=-uE_0,
$$
$$
N(u,\lambda,-u\lambda)+sE_0
=h\lambda\{(2u^2-7u+4)\lambda+3u-4\}.
\tag{15}
$$
当前 $u,h,\lambda$ 非零，故只剩原一次关系
$$
C\lambda=n,\qquad C=2u^2-7u+4,\quad n=4-3u.
\tag{16}
$$
$\gcd_{\mathbb Q[u]}(C,n)=1$，完整 QQ Bézout 已乘回；因此 $C=0$ 的整个纤维也被 (16) 排除，不是默默倒置一个未付头。

代入 $\lambda=n/C$ 后，
$$
C^2E_0(u,n/C)=2sF_4(u),
$$
$$
F_4(u)=2u^4-4u^3+9u^2-24u+16.
\tag{17}
$$
设
$$
S_{11}(u)=C^3 S(u,n/C,-un/C).
\tag{18}
$$
(12) 保证 (18) 是明确的 QQ 一元多项式，实际次数为 $11$。本次从 (12)、(16) 直接构建 (18)，完整 Euclid 返回
$$
\gcd_{\mathbb Q[u]}(F_4,S_{11})=1.
\tag{19}
$$
两个实际 Bézout 乘子的次数是 $10,3$，完整乘回为 $1$。这保留四次代数的全部复嵌入、重根和 (16) 的首项零纤维；没有以模空性提升特征零。

(17)、(19) 排空第二整支。合并 (10)，第一条原线性支 (5) 完整排空。

## 6. 新精确小源和实际身份

[自含源](../notes/2026-11-28-unit211-Phi-zero-true-Azero-first-linear-branch-original-return-8542.js)：

- blob b51011405fa503911b34031cdb627b6b440ba5cc；
- SHA256 5bbae7da8a21afec411666f9d2695bd33b58853f364c44dccda191b7148559de；
- 14154 字节，纯 V8 BigInt；
- 实际 170 ms；5577 次整数多项式乘法，60 次完整线性因子除法返回；
- 一元终端 26746 次有理运算、2557 次多项式乘法、8 次完整 Euclid 除法返回；
- 原 Gram、均值、N/P 和 jet 来源逐式返回；(14)、(17)、(19) 均为实际完成结果。

[小回执](../notes/2026-11-28-unit211-Phi-zero-true-Azero-first-linear-branch-original-return-execution-8542.json)同时准确保存两次未发布工程失败：第一次把已知来源 $E_1-E_W$ 错写成更强诊断 $E_1$；第二次把 variadic 多项式乘法 API 误传一个数组。它们均未返回新排除结论，修正的执行身份没有冒充旧源码成功。没有延长或重跑任何资源触界门。

独立静态复核也核对了真正 dual 平方、两个未倒置分支、完整 C 首项零和 QQ Bézout。成功源一条旧注释误述形式 q 的第二坐标；实际构造与正文 (7)、实际 meanCombo 均正确，冻结源码未改。

本条不依赖新 fd9 斜率计算的成败，也未重跑正确共同四头、旧错误 H1 或已冻结的 bf3 二元 GB。其互补范围是当前整 $A=0$ 的第二原线性支，仍须继续。
