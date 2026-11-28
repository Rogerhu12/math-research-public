# R150：正确 Phi 第二 NV 头与 ell=3/2 的整个原交集排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**结论。** 在当前正确 Phi、物理 $D\ne0$ 的原权图中，不存在同时满足
$$
B_2=\ell(3-2\lambda)+2T+2m\sigma=0,\qquad \ell=\frac32
\tag{1}
$$
的完整原点。唯一首次实际运行在整个四次常数域、整个 $u$ 二次及整个首一 $t$ 二次构成的 16 维代数中，返回了原理想中的 $1$。最终回到普通 $t$ 多项式环后，只有三条原均值式的乘子非零；其余五条完整原值的乘子均为零。

这里关闭的是 (1) 的整个交集。第二头其余权点、第一头及一般 $\ell=3/2$ 图不由本稿关闭。证明来自正确原 Gram 和完整 $NV$；旧 rank-one 的 $c=1/2$ 结论另有 $TB_3-A_2^2=0$、$h=1$ 前提，本稿没有采用它。

## 1. 原图、旧单位与两个 rho 分量

沿用正确 Phi 的
$$
s=u-1,\quad L=Q-2(u-1)(u-2),\quad
\ell=L/Q,\quad \delta=1-Q,\quad m=u-\ell .
$$
在 (1) 中准确有
$$
Q=-4(u-1)(u-2),\qquad \delta=(2u-3)^2,\qquad
m=(2u-3)/2,\qquad M=2(2u-3)^2.
\tag{2}
$$
取 $\rho=2u-3$，则
$$
b=1,\quad c=\frac12,\quad a_0=1-\ell=-\frac12,\qquad
p=2u-2,\quad q=4-2u .
\tag{3}
$$
另一 $\rho$ 分量交换两个 singleton 标签。后文同时保留两条 singleton 均值及全部 $N/P$ 值，因此同一原身份覆盖两个分量。

原单位 $u,Q,\delta,K_w=Q+4(u-1)$ 给本次纯 $u$ 支持
$$
U(u)=u(u-1)(u-2)(u-3)(2u-3),
\qquad K_w=-4(u-1)(u-3).
\tag{4}
$$
此外
$$
T_0=4(u-1)(u-3),\qquad P_{02}=3(u-1)Q.
$$
所有恢复分母均来自 (4)。最后实际目标是 $1$，未需要使用预定的正幂 $\{\lambda D\,t(f-u)\}^n$。

## 2. 两个完整原矩给精确四次常数代数

第二头给 $h+k=2\lambda-1$。设
$$
y=h+1,\qquad v=k-1,\qquad
\lambda=(y+v+1)/2,\qquad N(y)=y^2-8y+7.
$$
在 (3) 中，两原矩为
$$
E_2=(h-1)^2+\frac12(k-1)^2-A_\lambda,\qquad
E_3=(h-1)^3+\frac12(k-1)^3-B_\lambda,
$$
其中
$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1.
$$
普通多项式身份是
$$
2E_2=N-2yv,\qquad
7=2E_2+y(8+2v-y),
\tag{5}
$$
及
$$
P_4(y)=5y^4-48y^3+180y^2-276y+147
=6(N+2yv+2y^2)E_2-8yE_3.
\tag{6}
$$
首次源码在任何因式分解或商之前，完整返回了这两条二元身份。由 (5)，$y$ 在原两矩商中是单位；反向因 $P_4(0)=147$，在 $\mathbb Q[y]/P_4$ 中也可逆。因此有准确代数同构
$$
\mathbb Q[y,v]/(E_2,E_3)\simeq
K_4:=\mathbb Q[y]/P_4,\qquad v=N/(2y).
\tag{7}
$$

本次实际完整 QQ 因式分解及乘回，得到 $P_4$ 只有一个四次不可约因子，重数为一。故 $K_4$ 是完整四次域；计算保留其全部复数嵌入，没有选一个根。常数域上
$$
h=y-1,\qquad k=\frac{y^2-6y+7}{2y},
$$
$$
\lambda=\frac{3y^2-6y+7}{4y},\quad
T=\frac{5y^2-16y+7}{4y},\quad
w=\lambda-1-T=\frac{3-y}{2}.
\tag{8}
$$
程序重新核了两个原矩及
$$
D=\frac32A_\lambda-T^2=\frac12(h-k)^2.
\tag{9}
$$
该唯一常数因子没有因 $\lambda$ 或 $D$ 恒零被移除，而是进入了下述完整原值计算。

## 3. 完整 NV 返回一个真正 u 二次

记
$$
j=h+\frac k2=T+\frac32,\qquad
r=h+k+hk,\qquad R=(1-h)(1-k),\qquad E=A_1/2.
$$
正确原 $P_1,N_0$ 恢复化为
$$
E=-\frac{3(u-1)(u-2)}{u-3}j,\qquad
f=3(u-2)\lambda+\frac{3(u-2)^2}{u-3}j-(u-3),
$$
$$
V=f+t/2-E,\qquad W_1=T_0/2+2uf,\qquad
X=\frac{W_1-qV}{2\rho},\quad Y=\frac{pV-W_1}{\rho}.
\tag{10}
$$
同一个原 Gram 的四行为
$$
\begin{aligned}
g_0&=(0,0,p,q),\\
g_1&=(0,2E,X+p/2-t/2,Y+q/2-t),\\
g_B&=(p,X+p/2-t/2,0,t),\\
g_C&=(q,Y+q/2-t,t,0).
\end{aligned}
\tag{11}
$$
乘法是真正 dual germ 乘法
$$
(v_0w_0,\ v_0w_1+v_1w_0,\ v_Bw_B,\ v_Cw_C),
$$
迹为 $\tau(v)=a_0v_0+v_1+bv_B+cv_C$。以此定义原 $d=D_K1$、$F_2=\tau(d)=2f$ 及
$$
N_4(v)=2\tau(dv^2)-F_2\tau(v^2)
-4\tau(v)\tau(dv)+2F_2\tau(v)^2+\tau(vD_Kv).
\tag{12}
$$

对完整物理向量 $\mathbf V=(1,w,h,k)$，普通展开给
$$
N_4(\mathbf V)+2fE_2
=2\{-rf+RE+w[u(1+h-2k)+2(k-h)]\}.
\tag{13}
$$
其原来源可以直接检查：$d_1=f+E+u/2-t/2$，且
$$
\tau(\mathbf V D_K\mathbf V)
=2E+2hX+kY+2w(ph+qk/2)+(hk-h-k)t.
$$
利用 $h+k=2\lambda-1$，完整 $N_4$ 的 $X,Y$ 部分合成 $-2hkV$；代 (10) 后全部 $t$ 项精确相消。这里保留了原误差 $2fE_2$，没有用 $t=0$ 专门化替代原值。

定义
$$
F_u=3\lambda(u-2)(u-3)+3j(u-2)^2-(u-3)^2,\qquad
E_u=-3j(u-1)(u-2),
$$
$$
G(u)=-rF_u+RE_u+
w(u-3)\{u(1+h-2k)+2(k-h)\}\in K_4[u].
\tag{14}
$$
于是
$$
(u-3)N_4(\mathbf V)=2G(u)
\quad\text{在原两矩商中成立。}
\tag{15}
$$
本次 $G$ 的实际 $u$ 次数为 **2**。

为独立固定完整原来源，源码先在普通 $K_4[u,t]$ 中取 $H=(2u-3)(u-3)$，构造 $H$ 倍的 (11)。所有非恒定尺度只作精确多项式整除及乘回，未使用普通 $K_4[u]$ 中的非常数逆。由于 (12) 对 Gram 线性，实际完整返回
$$
N_{4,Hg}(\mathbf V)=2(2u-3)G(u),
\qquad F_{2,Hg}=2(2u-3)F_u .
\tag{16}
$$
第一式核了全部普通 $u,t$ 系数；其 $t$ 次数确为零。由 $u-3$ 既有单位，完整原 $NV=0$ 必须给 $G(u)=0$。

## 4. 整个 u 二次与原首一 t 二次

用 $G$ 在 $K_4$ 中的非零首项首一化，记
$$
g(u)=G(u)/\operatorname{lc}_uG,\qquad
A=K_4[u]/g(u).
\tag{17}
$$
本次实际检查 $g$ 与 (4) 的完整旧单位支持互素，**没有任何 paid primary removal**；余 $g$ 就是原首一二次。没有选择某个 $u$ 根，也没有取平方自由部分。$A$ 作为 $K_4$ 模自由秩二；它是否约化不作为论证前提。

所有 (10)–(11) 中的原分母，均在整个 $A$ 中通过 Bézout 及乘回给出真逆。随后在 $A[t]$ 中重新构造未缩放 Gram，并完整核
$$
E_0=0,\quad F_2=2f,\quad P_2(g_0)=P_{02},\quad
N_4(g_0)=2\lambda P_{02},\quad P_{\rm jet}=3wP_{02},
$$
以及完整 $N_4(\mathbf V)=0$。

使用[正确全权首一 t 二次](R150-appendix-unit211-Phi-zero-corrected-whole-monic-t-quadratic-exact-ten-columns-and-four-generator-NV-head.md)的实际原组合，令
$$
\mathcal R=(E_B+E_C/2-E_1)/2,\qquad
E_{Bo}=(E_B-E_C)/(2\rho),
$$
$$
q_t=\gamma_R\mathcal R+\gamma_OE_{Bo},\qquad
\gamma_R=-\frac{B_q}{\ell bc(u-1)Q},\quad
\gamma_O=-\frac{8\delta}{\ell},
$$
$$
B_q=Q^2+(2u^2-3)Q+2(u-1)(2u-1)(u-2).
\tag{18}
$$
源码实际返回 $q_t$ 对 $E_1,E_B,E_C$ 的三个普通原乘子，并核 $t^2$ 头严格为一。因此
$$
B=A[t]/q_t
\tag{19}
$$
是保全部 $t$ 重数的真实首一二次代数。其 QQ 维数为
$$
4\cdot2\cdot2=16.
$$
这里只说必要包络 $B$ 自由于逐层首一基；加入原条件后的商没有被假定自由。

## 5. 128 原列及最终普通多项式返 1

完整八个原种子按固定顺序为
$$
\begin{aligned}
F_1&=E_1,&F_2&=E_B,&F_3&=E_C,&F_4&=N_1,\\
F_5&=N_4(g_B)-2\lambda P_{02}h^2,&
F_6&=N_4(g_C)-2\lambda P_{02}k^2,\\
F_7&=P_2(g_B)-P_{02}h^3,&
F_8&=P_2(g_C)-P_{02}k^3 .
\end{aligned}
\tag{20}
$$
这里 $E_1$ 的平方项使用真正
$\operatorname{vm}(d,d)[1]=2d_0d_1$；
$N_1$ 是
$$
N_4(g_0+g_1)-N_4(g_0)-N_4(g_1)-4\lambda wP_{02}.
$$
两 singleton 的完整值均保留。

取 (19) 的 QQ 基
$$
y^a u^b t^c,\qquad 0\le a\le3,\quad 0\le b,c\le1.
\tag{21}
$$
每个 (20) 乘全部 (21)，得到 **128 条实际原列**。每条只按首一 $q_t$ 作普通除法，并以 (18) 的原乘子反传；全部 128 原列返回成功。这些列准确生成真实代数 $B$ 中的原理想作为 QQ 模。

实际有理线性代数给列秩 **16**，且预定的第一个目标 $1$ 已返回。程序随后将该目标和各列的首一除法商全部加回，经 (18) 再归入八个原式，最终在整个普通多项式环 $A[t]$ 中核得
$$
\boxed{1=\Omega_1E_1+\Omega_2E_B+\Omega_3E_C.}
\tag{22}
$$
三个 $\Omega_i$ 均有 $t$ 次数至多一、$u$ 次数至多一，常数系数在完整 $K_4$ 中。其余五个原乘子实际全为零。这里 (22) 是完整 $t$ 多项式回乘；不是只在 $q_t$ 的两个余坐标中返 1，也不是根据满秩或末尾布尔标志猜结论。

(22) 与 (17) 中完整 $G=0$、(15) 的原 $NV$ 来源及 (7) 的精确两矩同构相接，排整个 (1)。最后目标为 $1$，不需要借某个 $D,t,f-u$ 的幂零或逆来完成排除。

## 6. 全嵌入、重数和原题范围

本次 $P_4$ 实际只有一个不可约因子且重数一，全部四个常数嵌入同时在 $K_4$ 中保留。$u$ 的整个二次、$t$ 的整个首一二次均原样保留；未切换到某个复根或约化点集。另一 $\rho$ 分量通过完整 singleton 对换覆盖。

所以 (22) 是整个必要代数的单位返回，足以给当前物理原交集为空。它没有依靠独立范数的不同根被错误拼接，也没有恢复旧错误 Rbar 链。

作为直接后续应用，在当前正确第二头原点上，$\ell-3/2$ 不再有零点；该支付只限本稿第二头范围。一般第二头的剩余权图仍需新的原输入，第一头此前的三 scalar gcd 仍维持其已登记冻结边界。

## 7. 唯一实际执行与可核来源

- [冻结源码](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-head-ell-three-halves-whole-quartic-original-values-8542.py)：Git blob **c8e84e799c516e8d5fba5b88268440dcbd2b306d**；SHA256 **e9939ac41af3e0a5ef9080ef008519dc65cccb45fe1cd30f22a24d80767acfcb**。
- [执行前完整输入](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-head-ell-three-halves-whole-quartic-original-values-8542-input.md)：Git blob **c8cff464cb3c73c49fff58afde945492e6318fe7**。
- [小执行回执](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-head-ell-three-halves-whole-quartic-original-values-8542-execution.json)。
- [唯一首次 Actions run 46179464150](https://github.com/Rogerhu12/math-research-public/actions/runs/46179464150)，job **141085521543**，attempt **1**。

源提交 **5699f32c124a5a9c2ca57bf6305eb6a7cadbd01c**。驱动实际 pull 到 **949f09ab8fa42f99f9c27367ad11a25bb843fda4**，双 README 于 **2026-11-28 19:07:18.730294 UTC** 重新读取且未变。固定预算为 120 秒 / 1 GiB，外 135 秒；实际驱动 **6.4706440420000035 秒 / 39672 KiB / exit 0**，数学末记录 **6.400159822999996 秒**。

全文核读五条数学记录，并逐字重组 stdout：**5445 bytes**，SHA256
**581a769739aec06680794e655317293e48f3058ddcc577a21adb82bb40c79f39**，
与实际驱动一致。末状态为 closedFactors=[0]、unresolved=[]，其数学依据是上述完整原式返回。

关键实际摘要：

| 对象 | 实际范围 | SHA256 |
|---|---|---|
| 原 $P_4$ | 四次，唯一 QQ 不可约因子，重数一 | f99a2fe6211b1cd0d5be20ac15699c06fffb9492b1377fd5278fca889b7a2e34 |
| 完整 NV 权式 $G$ | $u$ 次数 2 | 63867f0a3a6953542346ee791876fea8b37e780eccb5d2dcd3305f16ab3e106c |
| 原及余首一 $g$ | $u$ 次数 2，无主分量删除 | 2e85aeba28c148d72cc91b0dbed8d1a86678d3c4fdc2f5269d4d4329bdee06ee |
| 原首一 $q_t$ | $t$ 次数 2，$u$ 次数 1 | 8aced3effc7efca638bf0ef84254c3df8c1d9821aa2f95361b6400c22572bed6 |
| $\Omega_1$ | $t,u$ 次数均 1 | ccfb3f7744684de9b87f129346b75a28e80e4e9aa6ee82cba65ae18935e2461d |
| $\Omega_2$ | $t,u$ 次数均 1 | 97590eba0ffec800f2240d2d476b591fd27db9c072b4e3a4263d85e2b527a03a |
| $\Omega_3$ | $t,u$ 次数均 1 | 751e8a27b04d37d1139a1fd7c6175e6d422eedbcb68ce9cb550df07e8175ce6d |

实际统计包括 5778 次常数域逆返回、158 次完整有限系数代数逆返回、49571 次多项式除法返回、128 原列、17 次有理向量返回及一次最终八原完整多项式返回。三个非零最终乘子由冻结源码的固定有理列选择、首一除法及反传公式定义；本稿及回执只保存 profiles，不保存系数载荷。

未执行草稿 a9070b121cb508ee452ceb6ff2dff3242ceae9aa 没有数学 run。本次只有 c8e84 的一次真实启动；没有重放旧六列、二十列、八条奇部列、第一头已冻 gcd，或任何资源失败门。
