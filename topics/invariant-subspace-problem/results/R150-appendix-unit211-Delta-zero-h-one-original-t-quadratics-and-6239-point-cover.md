# R150：Delta 零碰撞图的完整原 t 二次组合与 6239 基点覆盖

会话 Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。日期2026-11-27（Asia/Taipei）。

**结论：** 在一般 LS 原余图的 Delta*=0、zn=0 分支中，交换原 singleton 标签后取 h=1，原解的不同基参数对 (lambda,rho) 至多6239个。每对仍有至多三个原 ell 值；这里仅计参数投影，没有排除全部原解，也未证明原 t 在每一纤维只有有限选择。k=1 图按原标签交换保留，不把并图偷计同界。

## 1. 同一原来源

沿用[原首一 ell 三次、八值及八个 H³ 目标](R150-appendix-unit211-Delta-zero-h-one-monic-cubic-original-unit-and-degree-49-curve.md)和[F49及原兼容式本原性](R150-appendix-unit211-Delta-zero-h-one-original-degree-49-primitive-curve.md)。

底环只倒原已付的 lambda,rho,p,q,A2,B3,S。完整原关系为
$$
\Delta_*=0,\qquad C=\Phi N_C-S\zeta P_c=0,\qquad
H=bP_f\ne0,
$$
并保留 free 原 t。第一条按已付三次头首一化，在 1,ell,ell² 基底中完整运算；未删除重根或临时主元零纤维。

原 (C,ell C,ell²C) 与 H³ 组合已给
$$
F_{49}(\lambda,\rho)=0,\qquad
(\deg_\lambda,\deg_\rho)=(39,10).
$$
本次只再取同一 Gram 的 E1、EB 两行，用原 (C,ell C,E1) 和 (C,ell C,EB) 返回完整 H³ 目标。它们的全部最终标量分母清除后，只去掉已付基单位，得到必要式
$$
P(\lambda,\rho,t)=0,\quad Q(\lambda,\rho,t)=0
$$
（此处 Q 仅是多项式名称，不是原权 Q），准确次数为
$$
\deg_{\lambda,\rho,t}P=(92,23,2),\quad
\deg_{\lambda,\rho,t}Q=(73,21,2).
$$
两式分别6251项、4528项，来源与前稿必要式的SHA完全相同。本次没有重新生成后六原行或其余旧目标作为门槛。

## 2. 不除二次首项的完整多项式组合

仅在本节将这两个多项式记为
$$
P=at^2+bt+c,\qquad Q=dt^2+et+f,
$$
其中所有系数属于QQ[lambda,rho]。置
$$
L=ae-bd,\quad M=af-cd,\quad N=bf-ce,\quad
\mathcal R=M^2-LN.
$$
直接展开得到
$$
\boxed{
(dLt+eL-dM)P+(-aLt+aM-bL)Q=\mathcal R.
}
\tag{2.1}
$$
源实际核验完整 (2.1)，并核验右侧每个单项式都不含 ell 或 t。没有除以 a、d、L 或任何新参数因子。因此两个原二次首项分别或同时为零时，(2.1) 仍然成立。

实际原消元式 $\mathcal R$ 有27795项、双次数(326,84)、总次数410。仅移除已付因子
$$
p^2qA_2^6S_{\rm num}^3
$$
及非零有理常数，得到另一个必要式
$$
G_{389}(\lambda,\rho)=0,
\quad(\deg_\lambda,\deg_\rho)=(308,81),
\quad\deg_{\rm total}=389.
$$
它有25338项。所有整除都回乘，未剥除任何未知范数因子。两个真实组合标签对 t 都一次，分别28610项和31942项。

本次完整QQ计算准确返回
$$
\gcd_{\mathbb Q[\lambda,\rho]}(F_{49},G_{389})=1.
\tag{2.2}
$$
两原点必要式和 (2.2) 合用，而不是把一般多元 gcd1 当作无解。

## 3. 所有首项退化纤维上的有限计数

采用[2051点覆盖中的固定Sylvester核重数论证](R150-appendix-unit211-Phi-zero-rank-one-value-exact-core-2051-point-cover.md)，这里直接给出全部参数。

把 F49 和 G389 看成rho多项式，固定次数10、81。其完整91阶Sylvester矩阵在lambda上的非零行列式记R(lambda)；非零性来自 (2.2)。每个行列式项包含81个F49系数和10个G389系数，所以
$$
\deg R\le81\cdot39+10\cdot308=6239.
\tag{3.1}
$$
本次没有计算这个91阶行列式或其单变量系数。

任取lambda0。两式不能在整条该垂直线同时恒等零，否则存在共同垂直因子，违背 (2.2)。因此该纤维的不同有限共同rho根数r有限。每个根给Sylvester矩阵的实际求值核列，r个不同根的Vandermonde列独立。将这些列用常数可逆变换放到末r列，所得每列的条目都被lambda-lambda0整除，故
$$
\operatorname{ord}_{\lambda_0}R\ge r.
$$
这包含所有rho首项降次、重根及临时Cramer主元零纤维。对所有lambda0求和，(3.1)给不同原基点数至多6239。

原ell关系首一三次，故不同(lambda,rho,ell)投影至多18717个。原t和完整八行仍须逐纤维返回；上述计数未替代这一工作。

## 4. 实际执行与精确身份

- 源：`notes/2026-11-27-unit211-Delta-zero-h-one-full-original-t-quadratic-elimination-8542.py`。
- Git blob `641762f37d33db0ca4c3960886f15a6bc36c6478`，14458字节。
- SHA256 `1c2bf02e077d7fc32972491ddc5df4b91490258bf93e5fe0a748bb1117981534`。
- run45994622800/job140490805772，inner exit0。
- 驱动13.769811225秒，源13.709655105秒，RSS166460KiB；首次配置180秒/4GiB。
- 仅取E1、EB即取得 (2.2)，未继续展开EC、N1或全部八原行。
- stdout12090字节，SHA256 `228f4311b9071b4696d19d08aa5de567344ee33fd4560f3bded31bf654cecf0b`。
- 原 $\mathcal R$ 字符串5345900字节，SHA256 `8bbf57c60a6a9a8f00c3a668cf73ab8e45a4bc4ee4e1e9e7392d1df74715c2a1`。
- 必要 G389 字符串4625054字节，SHA256 `285f24269b20448bb3b0e2cafd652b659459100b26f7088e4240b9ccc28cd69a`。
- 2026-11-27 11:57:23.878501 UTC实际pull前后均 `c908a23aa20487693cffe202745871dd9f0b740f`，根与课题README无变。

只保存源码、小回执及全部规模/SHA，不保存可重算的大系数缓存。下一新输入为实际G389的精确整因子及原有限纤维，不重跑173秒八行门。
