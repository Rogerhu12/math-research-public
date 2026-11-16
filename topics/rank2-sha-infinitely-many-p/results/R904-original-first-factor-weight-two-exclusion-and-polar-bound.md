# R904 — 原第一因子的权二分母排除与权六截面的极除子下界

日期：2026-11-16。**状态：已证明。** 这里使用已经结束的原公开任务中的精确有限域满秩结论，证明同一原第一因子不能采用分母权二的表示。没有将权四重建预算耗尽解释为映射不存在，也不假定 Manin 常数为1。

## 1. 指定来源、参数和实际结果

原对象、归一和全部坐标定义均是 [R878](R878-original-first-factor-level867-coordinate-certificate.md)：
$$
X=X_0(10404),\quad B=X_0(867),\quad Q=q^6,\quad
E_{17}:y^2=x^3+17.
$$
原新形式为 $f(q)=qf_0(Q)$，$f_0=1-5Q-7Q^2-7Q^3+\cdots$。形式解满足
$$
X_{\rm form}^3=U^2-17Q,\qquad
2QU'-U=f_0X_{\rm form}^2,\qquad
X_{\rm form}(0)=1,\quad U(0)=-1.
\tag{1}
$$
令
$$
E(Q)=\prod_{n\ge1}(1-Q^n)^{12},\qquad
V_{\rm form}=E(Q)U(Q)=-1+5Q+\cdots.
\tag{2}
$$
若原归一的第一因子实际存在，则 $V=e(Q)y$ 是 $B$ 上亚纯权六截面，germ 恰为(2)。$V$ 不是权零有理函数；以下一直保留这个线丛区别。

公开执行的身份为：

- source：7920cb48d5b63b01a0d200c4a5ba584b128657aa；
- [run 43839815472](https://github.com/Rogerhu12/math-research-public/actions/runs/43839815472)，job 133205402538；
- producer：scripts/produce-r878-original-first-factor-map.py，该 source 的 blob 1a924680698cd1c0bbcf0c7eeeb1f67c8ad5ca4c；
- request：ci/original-first-factor-map-request.json，blob 5f321b2cb582cb4d3afeaaaaf4462376634f8499；
- 参数：--weights 2,4 --max-primes 96 --prime-start 1000000000 --product-prime 1000037，原固定 seed 20261116；
- pinned image：sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb。

09:39:25 UTC 的实际 RANK2_FIRST_FACTOR_CASE 给：
$$
k=2,\quad \text{rows}=1021,\quad \text{columns}=852,\quad
\ell=1000000007,\quad \operatorname{rank}_{\mathbf F_\ell}=852.
\tag{3}
$$
对应必要矩阵是原
$$
[Q^j](A-V_{\rm form}B_0),\qquad 0\le j\le1020,
\quad A\in M_8(867),\ B_0\in M_2(867).
\tag{4}
$$

完整输入身份还由以下已打印 hash 确定：

| 输入 | SHA-256 |
|---|---|
| $M_8$ 乘积 recipes | 80f6bffb12ab621aadb00579050b1f01d27654a418eef3654630563c4958e5a5 |
| $M_2$ recipes | cb2d348c8a1d6bfbe191e123520b6737a853472882088269df3f9b6b5dae8940 |
| (4) 所用 $M_8$ 有理 q 行 | 12b6a335cbceb50cce7fc8de0e491230014a40a8038d78fc443e629486a03ee9 |
| (4) 所用 $M_2$ 有理 q 行 | 7f776aefb31e58b266803abc518769007dd7ab7fd771f2643cee4daa1047e332 |

任务于15:27:10 UTC被取消。它没有打印完整最终 RESULT/SHA256；这里不虚构最终输出 hash。依根规则15，不将系数、矩阵或整份日志另存到仓库，精确脚本、参数和现有 run 足以重现(3)。

## 2. 为何这是完整空间而非某个子族

曲线 $B$ 无 elliptic points，指数1224、cusp 数36、亏格85。令
$$
\mathcal L=\Omega_B^1(\mathrm{cusps}),\qquad \deg\mathcal L=204.
$$
于是
$$
M_{2r}(867)=H^0(B,\mathcal L^r),\qquad
\dim M_{2r}=204r-84.
\tag{5}
$$
原 producer 从整个120维有理 $M_2$ 的有序基出发。对 $M_8$ 所选的732个实际四重乘积，在辅助素数1000037上的全部 $Q^0,\ldots,Q^{816}$ 行达到秩732；该事实在09:35:12 UTC的日志中打印。其 q 系数分母均在该素数处可逆。因此这些特征零形式线性独立。由(5)，它们已构成整个 $M_8$ 的有理基；不是把乘积空间的某个不足维子空间认作全空间。

$M_2$ 的120维和其前205项的满秩检查也先于(3)完成。换另一套完整有理基不会改变(4)是否存在非零核。

## 3. 从良好约化满秩到特征零排除

**命题。** 在任意特征零系数扩张上，不存在
$$
A\in M_8(867),\qquad 0\ne B_0\in M_2(867),
\qquad A/B_0=V_{\rm form}.
\tag{6}
$$

**证明。** (1)的三角递推见 R878(9)。到 $Q^{1020}$，除法只涉及3及 $6n+1$，$1\le n\le1020$；它们均小于$\ell=1000000007$，故为$\ell$单位。$f_0$ 与 $E$ 的输入系数为整数。原程序在进入(3)前又逐项检查了两个有理基的全部相关分母在$\ell$处可逆。

因此(4)是一个在$\mathbf Z_{(\ell)}$上定义的1021×852矩阵，其模$\ell$矩阵准确是程序用原递推建立的矩阵。由(3)，有一个852阶子式模$\ell$非零。该子式在$\mathbf Q$中非零，故原矩阵在$\mathbf Q$上列满秩。任意特征零标量扩张保留这个非零子式。

若(6)成立，将$A,B_0$用§2的完整基展开，便给(4)的非零核向量。即使$B_0$在 cusp 消失，恒等式$A-V_{\rm form}B_0=0$仍在所有这些系数成立，不能避开(4)。这与列满秩矛盾。证毕。

这里的有限窗只作为全局表示的必要条件，已经足够用于否定；不需要用有限窗代替原最终椭圆证书。

## 4. 条件性的极除子下界

**推论。** 如果(2)延拓为$B$上亚纯权六截面$V$，并记其作为$\mathcal L^3$截面的极除子为$R$，则
$$
\boxed{\deg R\ge120.}
\tag{7}
$$
特别$V$不是一个全纯$M_6$形式。

**证明。** 在任意代数闭特征零域上，完整有限除子序列给
$$
h^0(B,\mathcal L(-R))
\ge h^0(B,\mathcal L)-\deg R
=120-\deg R.
$$
若$\deg R\le119$，可取非零$B_0\in H^0(\mathcal L(-R))$。它消掉$V$的全部极，故
$$
A=VB_0\in H^0(\mathcal L^4)=M_8,\qquad
B_0\in H^0(\mathcal L)=M_2.
$$
这与§3矛盾。全纯$M_6$的情形正是$R=0$，因此同样被排除。证毕。

(7)是指定亚纯权六截面的极除子次数下界，不把它改称$V$作为权零函数的次数或原椭圆映射次数。

## 5. 权四重建实际到了哪里

同一任务在权四分母处使用完整的
$$
M_{10}\oplus M_4,\qquad
\dim=936+324=1260,\qquad \text{rows}=1429.
$$
最后一次实际日志为15:24:32 UTC：
accepted_primes=84，modulus_bits=2512，modular_rank=1116，
B_valuation=1，prime=1000001677。此前没有候选进入原完整特征零证书。

全部乘积基在约614秒已完成，长期工作发生在此后的原 germ/重建循环；日志没有拆开该循环的各子步骤，故不能将全部成本归给一个未单独计时的步骤。

权四没有满列秩证书，亦没有 PASS。下一条同原重建可以使用 R889 的已证明 Newton germ 及 R899 的固定素数 Dixon 机制，但必须保留：
$$
8\Delta C^3=\mathcal H B_0^2(A^2-17\Delta B_0^2)^2,
\quad
C=(D_QA)B_0-A(D_QB_0)-\tfrac12E_2AB_0,
$$
完整$Q^0,\ldots,Q^{6120}$、同一实际基的全前缀、$V(0)=-1$及$[Q]V=5$。本结果没有取得原第一因子、两真 map、真实 RR 或原 shadow。

## 附录 A. 由原权四全秩读数加强到极次数180

本附录只使用§1同一已结束的真实 run，不重跑数学、不猜重建结果。

在2026-11-16 09:43:11.6079054 UTC，原日志的首个权四 rational CRT 阶段准确给
$$
\ell=1000000007,\quad
\mathcal M_4\in M_{1429,1260}(\mathbf F_\ell),\quad
\operatorname{rank}\mathcal M_4=1116,\quad
\operatorname{ord}_Q B_0=1. \tag{A1}
$$
本节只用其中的秩；首自由坐标、$B_0$ 首阶和随后84个素数的 CRT 不是证明的额外假设。

同一日志已经输出完整 $M_4$ 和 $M_{10}$ 乘积基：

| 权 | 维数 | 全 Sturm 前缀项数 | recipes SHA-256 |
|---|---:|---:|---|
| 4 | 324 | 409 | 3cf33f7bca9c4966d3a6b9f62ec1654eda987f6d69d9350e063a7ceb43cd4d67 |
| 10 | 936 | 1021 | a062b680c5b08d5380cc41eb10cf41edcf68d91c23d24d0c52b468c5ed9e38b4 |

这些精确满基秩分别在09:32:46和09:38:04 UTC完成。已亲读§1的原 producer blob 1a924680698cd1c0bbcf0c7eeeb1f67c8ad5ca4c：在产生(A1)之前，它检查所有相关有理系数分母为$\ell$单位，并再次检查这两个完整基在$\ell$处各达到324和936秩。原递推至1428项的分母只有3及$6n+1$，也都是$\ell$单位。

所以(A1)准确是特征零矩阵
$$
\mathcal M_4:(A,B_0)\longmapsto
([Q^j](A-V_{\rm form}B_0))_{j=0}^{1428},
\quad (A,B_0)\in M_{10}\oplus M_4
\tag{A2}
$$
的好约化。一个1116阶子式模$\ell$非零，故在任意特征零标量扩张上
$$
\boxed{\dim\ker\mathcal M_4\le1260-1116=144.} \tag{A3}
$$
这里没有声称特征零秩恰为1116，也没有把模核维数144直接提升。

**命题A1。** 若原 $V_{\rm form}$ 延拓为 $B$ 上的亚纯 $\mathcal L^3$ 截面 $V$，其极除子 $R$ 必满足
$$
\boxed{\deg R\ge180.} \tag{A4}
$$

**证明。** 对每个 $B_0\in H^0(B,\mathcal L^2(-R))$，乘法给
$$
A=VB_0\in H^0(B,\mathcal L^5)=M_{10}.
$$
由原完整 germ，$(A,B_0)$ 满足(A2)的所有行。映射
$$
H^0(B,\mathcal L^2(-R))\longrightarrow\ker\mathcal M_4,\qquad
B_0\longmapsto(VB_0,B_0)
$$
因第二分量而单射。因此(A3)给该截面空间维数至多144。

另一方面，完整极除子的限制序列给
$$
h^0(B,\mathcal L^2(-R))
\ge h^0(B,\mathcal L^2)-\deg R
=324-\deg R.
$$
两式合并即 $324-\deg R\le144$，得到(A4)。以上论证包含全部有限位、cusps及其重数；$V$ 仍是权六截面。证毕。

**推论A2。** 若 R878(3) 的原归一化第一映射 $F_{17}:X_0(10404)\to E_{17}$ 确实存在，次数 $d_F$ 满足
$$
\boxed{d_F\ge1080.} \tag{A5}
$$

**证明。** 原覆盖$\pi:X_0(10404)\to B$次数18，且$\pi^*V=e\,y(F_{17})$。$e$ 在全部源 cusp 全纯，故
$$
\deg\pi^*R=18\deg R\le
\deg\operatorname{pole}(y\circ F_{17})=3d_F.
$$
所有分歧重数按拉回除子计入。代入(A4)即(A5)。证毕。

(A4)严格加强§4的120；(A5)才是原映射次数的条件下界，两者不混同。没有在此证明映射存在、$d_F$ 的具体值、完整核维数达到144或实际shadow非零。R905/R909仍须通过原特征零完整恒等式。
