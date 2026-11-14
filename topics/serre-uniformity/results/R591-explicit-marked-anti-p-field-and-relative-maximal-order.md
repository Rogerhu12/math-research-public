# R591：实际反循环 p 层的精确圆分模型、原标记与相对最大整环

**状态：已证明并完成精确复算；原 Norm 和普通类群标量仍未求。**
固定 R171 的 p=43、同一个 776 bit 素数 q、同一个 CM/Weil 标记。
本文给出实际反循环次数 43 域 K_t/K 的完整整数环、一个最大系数
408 bit 的精确整多项式、原生成元 t 的 Artin 校准，以及
F_t=F K_t 的完整相对整数环生成集。最后的原普通标量 b、lambda、
n、C、L 均未由本条求出。

2026-11-14 环境切换使旧 scratch 和 V8 store 都丢失。本稿和核验器
是**恢复新字节**，不声称恢复原 7295 字节稿或原 13204 字节源码。
从仓库原 R171 输入重新执行一次精确算法后，核心多项式和乘法矩阵
的逐字序列化 SHA 与中断前冻结值完全一致，见第 8 节。
本恢复不依赖旧 Arb 的另一个 156 bit 生成元模型。

## 1. 从普通圆分单位构造实际反循环域

令

$$
 K=\mathbf Q(i),\quad Z=K(\zeta),\quad \zeta=\zeta_{43},
 \qquad u_a=-i\frac{1-i\zeta^a}{1+i\zeta^a}
 \quad(1\leq a\leq42).
$$

分子、分母在 Z/K 的范数分别为 i 和 -i，故它们是普通单位；
u_a 也是普通单位。直接化简给 u_{-a}=u_a^{-1}。在固定复嵌入中

$$
 u_a=-\tan\left(\frac\pi4+\frac{\pi a}{43}\right)\in\mathbf R.
$$

设 e_a 为 a^{-1} 模 43 的中心代表，-21<=e_a<=21，并置

$$
 \epsilon=\prod_{a=1}^{42}u_a^{e_a}
          =\prod_{a=1}^{21}u_a^{2e_a},\qquad
 \rho=\epsilon^{1/43}>0.
 \tag{591.1}
$$

epsilon 的全部实共轭为正。对 b 属于 F_43^times，记
sigma_b(zeta)=zeta^b，sigma_b(i)=i。逐项重排给

$$
 \frac{\sigma_b\epsilon}{\epsilon^b}=r_b^{43},\qquad
 r_b=\prod_{a=1}^{42}u_a^{(e_{b^{-1}a}-be_a)/43}>0.
 \tag{591.2}
$$

指数都是整数；配对 a 与 -a 后还说明 r_b 的各实共轭为正。
因此

$$
 \widetilde\sigma_b\rho=r_b\rho^b
$$

给一个阶 42 的 tame 截面：复合后对 rho 的像是同一个正的
43 次根，故群律准确成立。若 gamma(rho)=zeta rho，则
tilde-sigma_b 与 gamma 交换，因为两边作用于 rho 都产生 zeta^b。

第 3 节的有限剩余符号证明 epsilon 不是 43 次幂。因此

$$
 K_t=Z(\rho)^{\langle\widetilde\sigma_b:b\in\mathbf F_{43}^\times\rangle}
 \tag{591.3}
$$

是 K 上循环 43 次扩张。圆分单位的整性说明它在 43 外不分歧。
取 i->-i、zeta 不变、rho->rho^{-1} 的 involution；它反演 gamma。
它与真正复共轭只差 tame 截面中的 sigma_{-1}，所以在 K_t 上
就是原复共轭。于是 K_t/K 是反循环扩张。

K 的类数为 1。K_43/Q_43 未分歧二次，p-adic logarithm 给
U_1^{43}=U_2；阶 43 的局部角色因而导子至多 (43)^2。
非平凡性、43 外不分歧和类数 1 迫导子恰为 (43)^2。
该射线群的反变 43 商只有一维，所以 (591.3) 就是已有 CM
p^2 射线域的实际反循环次数 43 子域；第 3 节再校准其生成元。

## 2. 完整整数基及 43 次固定子域

记 rho_a=tilde-sigma_a(rho)>0，并定义

$$
 \theta_j=\sum_{a=1}^{42}\zeta^{aj}\rho_a
 \quad(j\bmod43).
 \tag{591.4}
$$

theta_0 被 tame 截面和复共轭固定。gamma theta_j=theta_{j+1}，
tau theta_j=theta_{-j}，并且 sum_j theta_j=0。
rho_a rho_{-a}=1 给准确的迹公式

$$
 \operatorname{Tr}_{K_t/K}\theta_j=0,\qquad
 \operatorname{Tr}_{K_t/K}(\theta_j\theta_k)
 =43(43\delta_{jk}-1).
 \tag{591.5}
$$

因此 1,theta_1,...,theta_42 的迹 Gram 行列式为 43^84。
这些元均整。导子-判别式公式另一方面给
disc(K_t/K)=(43)^84，因为 42 个非平凡角色的导子都是 (43)^2。
故

$$
 \mathcal O_{K_t}=\mathcal O_K\{1,\theta_1,\ldots,\theta_{42}\}.
 \tag{591.6}
$$

此处确实是完整基。theta_0 的 43 次多项式还在第 4 节通过模 5
不可约性独立核验。

H_t=K_t^{tau} 的签名为 (1,21)，不是全实域。完整 Z 基为

$$
 1,\quad B_j=\theta_j+\theta_{-j},\quad
 C_j=i(\theta_j-\theta_{-j})\quad(1\leq j\leq21).
$$

这是 (591.6) 在 tau 下的准确不变量格。其 Gram 矩阵为

$$
 [43]\oplus(2\cdot43^2I_{21}-4\cdot43J_{21})
       \oplus(-2\cdot43^2I_{21}),
$$

从而 disc(H_t)=-2^42*43^84。
若同时把 zeta 换成 zeta^d、rho_a 换成 rho_{ad}，(591.4) 的
theta_j 全部保持不变。这允许使用 R171 原 Weil 根而不改 t。

## 3. 原 t、beta 及正 Artin 的精确校准

沿用 primary beta=-1+2i，N beta=5。在 O_K/(beta)=F_5 中 i=3。
ord_43(5)=42，Phi_43 在 F_5 不可约。核验器在这个准确的
42 次有限域中计算得

$$
 \epsilon^{(5^{42}-1)/43}=\zeta^{22}\ne1.
 \tag{591.7}
$$

这是 beta 的 Frobenius 的第 42 次幂。故 K 上的正 Artin 在
gamma 坐标为 22/42=21 模 43。

另一方面，Gaussian 整数精确乘方给

$$
 \beta^{1848}=904+1376i
           =1+43(21+32i)\pmod{1849}.
$$

因 1848=-1 模 43，原协变 CM 第一对数为 -(21+32i)。
原 t=1+21pi 在反循环商中的坐标为 1，故 beta 的该坐标是
-32/21=21 模 43。两边在非零点 beta 上一致，所以

$$
 \boxed{\gamma=t,\qquad\kappa_p(t)=1.}
 \tag{591.8}
$$

这不是只识别未标记的循环域。scalar S 与 anti T 两个 p 方向
没有被混同；也没有把 22 直接当底域 Artin 值。

## 4. 精确整乘法矩阵与 408 bit 多项式

以下算法完全在 Z[i][zeta]/Phi_43 中执行。首先直接展开

$$
 u_d=i+(1-i)\sum_{v=0}^{42}(-i)^v\zeta^{dv}.
 \tag{591.9}
$$

对 a=2,...,42，b=1-a，置

$$
 m_{a,d}=\frac{e_{a^{-1}d}+e_{b^{-1}d}-e_d}{43}
 \in\{-1,0,1\},\qquad
 h_a=\prod_{d=1}^{21}u_d^{2m_{a,d}}
     =\frac{\rho_a\rho_b}{\rho_1}.
$$

并以幂基 1,zeta,...,zeta^41 写

$$
 H_k=\sum_{a=2}^{42}\zeta^{(1-a)k}h_a
    =\sum_{ell=0}^{41}m_{k,ell}\zeta^{ell}.
$$

展开 theta_0 theta_k、先分离 a+b=0 的项，再把其余项按
d=a+b 重排，得到准确恒等式

$$
 \theta_0\theta_k=(42\text{ if }k=0,\ -1\text{ otherwise})
                   +\sum_{ell=0}^{41}m_{k,ell}\theta_{ell}.
 \tag{591.10}
$$

在 (591.6) 的基下，乘 theta_0 的 43*43 矩阵 M 的第零列是
(0,-1,...,-1)^t。对列 k=1,...,42，常数行是 -1，行 j=1,...,41
是 m_{k,j}-m_{k,0}，最后一行是 -m_{k,0}。
全部条目为 Gaussian 整数，最大坐标仅 26 bit。

核验器逐次执行整 Faddeev-LeVerrier 递推：每次除以
1,...,43 都核准两个坐标整除，所有特征多项式系数虚部为零，
最后的 Cayley-Hamilton 矩阵严格为零。所得首一 43 次多项式
P_theta 的最大系数为 408 bit。
模 5 再核准 gcd(P_theta,X^5-X)=1 及 X^(5^43)=X，因 43 素而
得不可约性。全部整数系数和完整矩阵都保存于证书，不以哈希代替数据。

在同一整数基中，t 的作用特别简单：

$$
 (c_0,c_1,\ldots,c_{42})\longmapsto
 (c_0,-c_{42},c_1-c_{42},\ldots,c_{41}-c_{42}).
 \tag{591.11}
$$

## 5. 同一个 q 素点上的 43 个精确分支

使用 R171 原 q、原 zeta=e_43(P,iP)，绝不对 776 bit 整数做
JavaScript Number 转换。因为 q=-1 模 172，u_a 在 F_q 内；
43 与 q-1 互素，所以各个 epsilon_a 在 F_q 内有唯一 43 次根。
以它们代入 (591.4) 得 43 个互异的 theta_j 根，并且

$$
 \theta_j^q=\theta_{-j}.
$$

只有 theta_0 属于 F_q，其准确值为

```text
148744992525694032252153033135038096685773870238183621798369636318237346986286226806884168316917318315826907918769500752959749152696299669679028280219160288356458960197068546157018804422255134115675506563630593485021850459734196136450
```

每个根都代入完整 P_theta 核零；更强地，对每个分支的整个
43 维评价向量 ev_j，逐列核准 ev_j M=theta_j ev_j，合计
1849 个矩阵列等式。这既检验乘法，也保留全部 t 分支的顺序。

唯一 F_q 根对应唯一 tau 稳定的 q 素点。R171 已固定 F 的同一
tau 稳定点，R204 第 3 节固定纯 p 塔相同的实分支；因 43 为奇数，
此处不能再任意平移 t^j 后仍称作同一个实 q 分支。

## 6. F_t/F 的局部最大整环与 different

取 R171 的同一个 y=y_F，其多项式写成

$$
 P_F(Y)=Y^{44}+43R(Y).
$$

它在 43 Eisenstein，R(0)=5 模 43，故 y 是 F 在 p 上的一致化元，
v_F(43)=44。令 pi_t=theta_0+1，其多项式为
g(X)=P_theta(X-1)=sum_{j=0}^{43} a_j X^j。
精确的 44 个系数给：

- v_43(a_0)=1；
- 1<=j<=40 时 v_43(a_j)=2，唯一例外 j=17 为 3；
- a_41=0、a_42=-43、a_43=1。

所以 g Eisenstein，pi_t 是 K_t 在 p 的一致化元；g'(pi_t)
的最低赋值唯一来自 j=42，为 43+41=84。

因为 [F:K]=44 与 [K_t:K]=43 互素，F_t=F K_t 的相对次数是 43。
置

$$
 z=\frac{\pi_t}{y},\qquad h(Z)=\frac{g(yZ)}{y^{43}}.
 \tag{591.12}
$$

非首项的 v_F 为 44v_43(a_j)+j-43。常数项为 1，Z^42 项为 43，
其余非零非首项至少为 46；因此 h 是真正的相对 Eisenstein
多项式，1,z,...,z^42 是完整局部整数基。

在 F_t 中用 v(z)=1 归一，h' 的 j=42 项赋值为
43*43+41=1890，首项 43z^42 为 43*44+42=1934，
其余非零项至少为 1978。最低项唯一，故

$$
 d(F_t/F)=1890=42\cdot45,
 \quad\text{lower break}=44,
 \quad\text{conductor exponent}=45.
 \tag{591.13}
$$

简单 tensor order 的相对判别式赋值为 44*84=3696，故其局部
index 赋值是 (3696-1890)/2=903=sum_{j=1}^{42}j。
不能把旧 tensor order 当作最大整环运行 Norm 算法。

## 7. 完整全局整数环生成集

以升幂顺序取 A(Y) 的 44 个系数为

```text
26,0,39,0,12,0,30,0,20,0,26,0,4,0,25,0,24,0,0,0,26,0,
20,0,13,0,15,0,38,0,26,0,7,0,38,0,36,0,12,0,16,0,26,0
```

核验器先求 R 的逆模 (43,Y^44)，再在 Z[Y]/P_F 作整多项式乘法
及约减，逐系数检查

$$
 R(y)A(y)=1+43B(y),\qquad B(Y)\in\mathbf Z[Y].
 \tag{591.14}
$$

因此 R(y)A(y) 是 p 局部的单位。定义

$$
 w_j=-\frac{\pi_t^j y^{44-j} A(y)}{43}
     =z^j R(y)A(y)\quad(1\leq j\leq42).
 \tag{591.15}
$$

在 p 处，1,w_1,...,w_42 与局部最大基只差对角单位，故仍为完整基。
在 p 外，表达式左侧只有分母 43，故每个 w_j 整；而 K_t/K 在
p 外有限 etale，基变换到正常环 O_F 后仍正常，所以旧 tensor
order 在这些素点已经最大。各处局部化相同遂给

$$
 \boxed{\mathcal O_{F_t}
 =\mathcal O_F\mathcal O_{K_t}
       +\sum_{j=1}^{42}\mathcal O_F w_j.}
 \tag{591.16}
$$

这是 85 个 O_F 生成元。这里 O_F 指**实际最大整环**；没有把
Z[y] 冒作 O_F，也没有声称 85 项是自由基。
QC 已独立核对这个局部/全局拼接论证、different、index 和生成数。

## 8. 恢复证书与实际范围

原 R171 输入的 SHA256 为

```text
a3197f9b17672017a2e49072cfcdab7b1a07813c15eb3a73de2aa0093ef86aa6
```

恢复核验器检查该 SHA、正确 alpha_F=89460y_F+1 的范数 -q、
全部圆分恒等式、整矩阵、多项式、beta 标记、q 分支、局部赋值及
全局 A 逆。一次恢复运行已经全部 PASS；原 q 素性沿用 R171 已发表
ECPP/Pratt 证书，不把重复跑已验证素性链当成新数学结果。

按紧凑 JSON 加一个换行序列化，恢复后的两个核心哈希准确是

| 核心数组 | 与旧冻结值一致的 SHA256 |
|---|---|
| 多项式升幂十进制字符串数组 | `601aeade1625cb2b533d10a9a45e00407ffe40a6b730eeb004acbf5c4a819b14` |
| 逐行 Gaussian 坐标字符串矩阵 | `8a663ac35d6a7066ed57f2aaf9a98eb9eb3cd25f1775fc7a9c865ee69ed3e547` |

新的 proof/source 及五份 JSON 因元数据组织不同而采用新 SHA，
完整记录在 recovery validation 与 manifest 中。

- [精确核验器](../scripts/verify_r591_explicit_anti_p_field.js)
- [完整圆分代数](../notes/r591_exact_cyclotomic_algebra.json)
- [beta 标记](../notes/r591_exact_beta_marking.json)
- [原 q 分支](../notes/r591_exact_cyclotomic_q_marking.json)
- [相对局部模型](../notes/r591_relative_local_norm_model.json)
- [全局整环生成集](../notes/r591_global_maximal_order_generators.json)

```sh
node scripts/verify_r591_explicit_anti_p_field.js \
  --r171 notes/r171_principal_norm_selflocal_certificate.json \
  --out-dir notes --check
```

现在可以在准确整数环中写出真正的相对方程

$$
 \det_F(M_X)=89460y_F+1,\qquad X\in F_t.
$$

但本条没有找到这个 X。即使以后解出这个 alpha_F 的 Norm，它也
不是 R201 所求 L/F 的 Robert 单位 u 的 Norm，仍须证明同一标记、
完整外支撑和互反系数的连接。本文不将旧首阶 10、纯 p 的 24、
ray-T 系数或一个未主化的理想替代原普通 b。

### 来源

R171 提供原 F、q、alpha_F 和 Weil 标记；R196 第 3 节及
R204 第 3 节提供原 kappa_p、正 Artin 和实 q 分支的规范。
本文的整数矩阵、有限域校准、完整整数基和局部不同均已在上文证明。
所用标准类域工具为导子-判别式公式、射线类域对应和
Hasse Norm theorem，可参 J. S. Milne, *Class Field Theory* v4.03：
<https://www.jmilne.org/math/CourseNotes/CFT.pdf>。

