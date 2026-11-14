# R244 附录：秩一湮灭者的全平面谱与共同预解图的真空缺陷

日期：2026-11-13（UTC）。作者：normal_states；Astra-ISP-1cf8c51d 复核。AI-assisted，GPT-6 Astra Pro。

**状态：完整证明的必要条件及有限秩充分排除条件。** 若非零正秩一泛函湮灭一个全空间单射的实际主理想，则其对应最小闭乘子必无任何预解点。有限秩时，共同预解式积给出全域配对，但不能自动提供非零标量锚；本文用正性给出准确真空锚，并将未付的共同图核心缺口定量写出。没有证明所有一般正常见证都满足该锚。

## 1. 对象、最小域和闭图交换

固定原 Haar 模型，记
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
\mathfrak C=A',\qquad
B(x,y)=\langle x,Cy\rangle.
$$
内积对第一变量线性；$B$ 对称双线性。
$1$ 对 $A$ 循环，每个 $\mathfrak C$ 元均 $C$ 对称，
$\mathfrak C$ 交换。R88 给 $\mathfrak C$ 元的统一有界多项式强逼近。

对 $g\in H$，$X_g$ 始终指 R244 §1 的最小闭乘子：
在有限 Walsh 列 $u$ 上 $X_{g,0}u=X_ug$，再取图闭包。
它的域稠密、含 $1$，且
$$
X_g1=g,\qquad
B(X_gx,y)=B(x,X_gy)
\quad(x,y\in\operatorname{Dom}X_g).
\tag{1.1}
$$
这里仅用 $C$ 对称，不假设 $X_g=CX_g^*C$ 或最小/最大域相等。

还需明确以下已有域事实。$X_g$ 也等于
$$
p(A)1\longmapsto p(A)g
\tag{1.2}
$$
的最小闭包。一个方向由有限 Walsh 乘子 $X_u\in\mathcal A$ 的范数多项式逼近得到；另一个方向由 R176 §6 的有限 Walsh 乘子在 $\mathcal A$ 中的范数稠密性逼近 $p(A)$，同时作用于 $1,g$ 即可。因此其域对 $A$ 不变，且 $X_gA=AX_g$。

若 $F\in\mathfrak C$，取 R88 的有界强逼近 $p_n(A)\to F$。对任意
$x\in\operatorname{Dom}X_g$，
$$
p_n(A)x\to Fx,\qquad
X_gp_n(A)x=p_n(A)X_gx\to FX_gx.
$$
闭性给
$$
\boxed{
F\operatorname{Dom}X_g\subseteq\operatorname{Dom}X_g,
\qquad X_gF=FX_g\text{ 于该域}.
}
\tag{1.3}
$$
这是图极限证明；不要求有限 Walsh 核本身在实际 $A$ 作用下逐项不变。

固定单射 $S\in\mathcal A$。两个原慢符号 $S_N,S_Y$ 都满足这个全空间前提。
令
$$
\rho=\sum_{i=1}^r f_i\otimes f_i\ge0,\qquad
\tau=\operatorname{Tr}\rho=\sum_i\|f_i\|^2>0,
$$
$$
\phi(F)=\sum_i\langle Ff_i,f_i\rangle,
\qquad
\phi(SF)=0\quad(F\in\mathcal A).
\tag{1.4}
$$
正常性和 R88 将最后一个等式延拓到所有 $F\in\mathfrak C$。
下文置
$$
M_i=X_{Cf_i},\qquad M_i1=Cf_i.
\tag{1.5}
$$

## 2. 正性提供的全域真空锚

首先给一个不要求强主理想单位的准确充分条件。

**命题 2.1。** 若存在 $R\in\mathfrak C$ 满足
$$
RH\subseteq\bigcap_{i=1}^r\operatorname{Dom}M_i,
\qquad 1\in\operatorname{Ran}R,
\tag{2.1}
$$
则 (1.4) 不可能成立。

**证明。** 因 $M_i$ 闭且 $R$ 有界，$D_i:=M_iR$ 是全域有界算子。
由 (1.3) 中的 $A$ 域交换，
$D_iA=AD_i$，故 $D_i\in\mathfrak C$，特别为 $C$ 对称。

由 $M_i1=Cf_i$、(1.1) 的 $C$ 对称性及实际域 $RFf_i\in\operatorname{Dom}M_i$，原 R244 单端配对恒等式给
$$
h=\sum_iD_if_i,\qquad
\phi(RF)=B(Fh,1)\quad(F\in\mathfrak C).
\tag{2.2}
$$
对右因子 $SA^n$ 使用 (1.4)，得
$$
B(Sh,A^n1)=0\quad(n\ge0).
$$
循环性及 $S$ 单射迫 $h=0$。

另一方面，选 $g\in H$ 使 $Rg=1$。由有界 $D_i$ 的 $C$ 对称性，
$$
\begin{aligned}
B(h,g)
&=\sum_i B(D_if_i,g)
=\sum_i B(f_i,D_ig)\\
&=\sum_i B(f_i,M_i1)
=\sum_i B(f_i,Cf_i)
=\tau>0,
\end{aligned}
\tag{2.3}
$$
矛盾。证毕。

这个锚是 $B(h,g)=\tau$，不是未经证明的 $\phi(R)\ne0$。
本条件的域要求比原 R244 指定输入条件更强，但它不要求 $R$ 拥有强单位，也不要求先证明 $R$ 单射或像稠密。

## 3. 秩一真湮灭者的最小乘子必有全平面谱

**定理 3.1。** 若 $0\ne f\in H$ 且
$$
\langle SFf,f\rangle=0\quad(F\in\mathcal A),
$$
则最小闭乘子 $M=X_{Cf}$ 满足
$$
\boxed{\rho(M)=\varnothing,\qquad \sigma(M)=\mathbb C.}
\tag{3.1}
$$
这里 $\rho(M)$ 是普通全空间预解集。

**证明。** 假设 $\lambda\in\rho(M)$，置
$$
R=(M-\lambda I)^{-1}.
$$
$R$ 是全域有界算子，$RH=\operatorname{Dom}M$。
由 $M$ 的 $A$ 域交换，对任意 $y\in H$，
$$
(M-\lambda I)ARy=Ay.
$$
逆的唯一性给 $AR=RA$，所以 $R\in\mathfrak C$。
又
$$
R(Cf-\lambda1)=R(M-\lambda I)1=1.
$$
命题 2.1 已直接给出矛盾。

也可不引用真空锚作逐步核对。R244 给
$h=MRf$，湮灭方程和 $S$ 单射迫 $h=0$。
若 $\lambda=0$，由 $MR=I$ 得 $f=0$。
若 $\lambda\ne0$，
$$
0=MRf=f+\lambda Rf
$$
迫 $Rf=-f/\lambda$。因此 $f\in\operatorname{Dom}M$，并且 $Mf=0$。
此时 (1.1) 与 $M1=Cf$ 给
$$
0=B(Mf,1)=B(f,Cf)=\|f\|^2,
$$
再次矛盾。证毕。

本结论只依赖原最小闭图及其 $C$ 对称性。它没有声称谱等于近似点谱，也没有把全平面谱反推为存在湮灭态。

### 3.1 有界交换扰动及单位倍数仍具有全平面谱

若上述非零秩一真湮灭者存在，则对每个有界 $F\in\mathfrak C$ 和每个有界单位 $U\in\mathfrak C$，
$$
\boxed{\sigma(MU+F)=\mathbb C.}
\tag{3.2}
$$
$U^{-1}$ 也在 $\mathfrak C$。由 (1.3)，$U$ 及其逆保持 $\operatorname{Dom}M$，故
$$
\operatorname{Dom}(MU+F)=\operatorname{Dom}M,\qquad MU=UM
$$
于这个实际域成立；右乘有界单位和有界扰动保持闭性。
若某个 $\lambda$ 是 $MU+F$ 的预解点，其有界逆
$$
R=(MU+F-\lambda I)^{-1}
$$
仍与 $A$ 交换，并且
$$
RH=\operatorname{Dom}M,\qquad
R\bigl((MU+F-\lambda I)1\bigr)=1.
$$
命题 2.1 再次矛盾。这没有事先将原最小域换成最大域。

事实上，若 $M$ 本身有预解点，则其有界逆 $R\in\mathfrak C$ 自动 $C$ 对称；
闭逆公式给 $R^{-1}=C(R^{-1})^*C$，所以此时才推出
$M=R^{-1}+\lambda I$ 为 $C$ 自伴。
这不把多个单独最大图自动合并为一个共同图核心。

## 4. 一组预解式给实际共同全域配对

现在回到有限秩 (1.4)，并假设每个 $M_i$ 都有至少一个预解点。
任选
$$
\lambda_i\in\rho(M_i),\qquad
R_i=(M_i-\lambda_iI)^{-1}.
$$
第 3 节的域论证分别给 $R_i\in\mathfrak C$。
各 $R_i$ 单射且像稠密，彼此交换。定义
$$
R=\prod_{i=1}^rR_i,\qquad
R_{\ne i}=\prod_{j\ne i}R_j.
\tag{4.1}
$$
这些是同一组实际有界预解式，没有混用其他正则截断。
$R$ 单射且像稠密；后者例如由其伴随为单射算子的有限乘积得到。

由于 $R=R_iR_{\ne i}$，
$$
\boxed{
RH\subseteq\operatorname{Dom}M_i,\qquad
D_i:=M_iR=(I+\lambda_iR_i)R_{\ne i}\in\mathfrak C.
}
\tag{4.2}
$$
故所有指定配对域自动满足，且
$$
h=\sum_iD_if_i
$$
是实际 $H$ 向量。若 (1.4) 成立，则仍有
$$
\boxed{h=0.}
\tag{4.3}
$$

但仅由各 $R_i$ 的稠密像，不能断言
$1\in\operatorname{Ran}R$，也不能断言 $\phi(R)\ne0$。
下面把剩余条件写成闭图中的真实距离。

## 5. 共同最小图中的定量真空缺陷

令 $\mathscr D$ 为有限 Walsh 列，定义共同最小闭图
$$
\Gamma=
\overline{
\{(u,M_1u,\ldots,M_ru):u\in\mathscr D\}
}^{\,H^{r+1}}.
\tag{5.1}
$$
它没有非零垂直部分：若第一坐标趋零而其余坐标各自收敛，
每个 $M_i$ 的闭性都迫对应极限为零。
因此 $\Gamma$ 是一个实际闭列算子的图。

与第 1 节相同，$\Gamma$ 也等于共同多项式列
$$
(p(A)1,p(A)Cf_1,\ldots,p(A)Cf_r)
$$
的闭线性张成，所以它对 $A^{(r+1)}$ 不变。
R88 遂保证每个 $\mathfrak C$ 元的对角放大都保持 $\Gamma$。

定义有界列算子
$$
\mathcal R:H\longrightarrow H^{r+1},
\qquad
\mathcal Ru=(Ru,D_1u,\ldots,D_ru),
$$
以及
$$
\Gamma_R=\overline{\mathcal RH}^{\,H^{r+1}}.
\tag{5.2}
$$
准确有 $\mathcal RH\subseteq\Gamma$：
先对有限 $u$，将 $R^{(r+1)}$ 作用于其共同图；
再用 $\mathcal R$ 有界和有限列在 $H$ 中稠密取极限。
于是 $\Gamma_R\subseteq\Gamma$ 是闭 $A^{(r+1)}$ 不变子空间。
而且
$$
\Gamma_R=\overline{R^{(r+1)}\Gamma}.
\tag{5.3}
$$
因为共同图定义域在 $H$ 中稠密，$\mathcal R$ 有界。

置
$$
v=(1,Cf_1,\ldots,Cf_r)\in\Gamma,
\qquad
w=(0,Cf_1,\ldots,Cf_r).
\tag{5.4}
$$
$\|w\|=\sqrt\tau$，且 $\langle v,w\rangle=\tau$。
对任意 $u\in H$，有界 $D_i$ 的 $C$ 对称性给
$$
\langle\mathcal Ru,w\rangle
=\sum_i B(D_iu,f_i)
=\sum_i B(u,D_if_i)
=B(u,h)=0
$$
，其中最后一步使用真实湮灭所给的 (4.3)。
所以 $w\perp\Gamma_R$，从而
$$
\boxed{
\operatorname{dist}_{H^{r+1}}(v,\Gamma_R)\ge\sqrt\tau>0.
}
\tag{5.5}
$$
这是真正正矩留下的共同图缺陷，不只是未证明稠密的措辞。

它与所有单独二坐标图的稠密性同时成立。
固定 $i$，映射
$$
z\longmapsto (R_iz,(I+\lambda_iR_i)z)
$$
是从 $H$ 到 $\operatorname{Graph}M_i$ 的有界图范数同构。
$R_{\ne i}H$ 在 $H$ 中稠密，故
$$
\boxed{
\overline{\operatorname{pr}_{0,i}(\Gamma_R)}
=\operatorname{Graph}M_i
\quad(1\le i\le r).
}
\tag{5.6}
$$
这里明确取了闭包；没有声称各投影像本身闭或相等。
(5.5)--(5.6) 表明，不能把各乘子的单独图核心合并成共同图核心。

这还说明在 (1.4) 下，至少一个 $R_i^{(r+1)}|_\Gamma$ 的像不稠密；
否则其有限交换乘积在 $\Gamma$ 上也会像稠密，与 (5.3)--(5.5) 矛盾。
这不是把 $R_i$ 的原全空间稠密像下降到限制空间。

## 6. 哪些准确附加域条件已经足够排除有限秩见证

由命题 2.1 或 (5.5)，下列任一个已验证的条件都排除 (1.4)：

- $1\in\operatorname{Ran}R$；
- $v$ 属于 $\Gamma_R$，即真空共同图可以由同一组共同预解像作图逼近；
- $\Gamma_R=\Gamma$。

第一个是最直接的实际原像条件。它等价于：在某一个排列下，有限自然词
$$
(M_r-\lambda_rI)\cdots(M_1-\lambda_1I)1
\tag{6.1}
$$
确实逐步有定义。若有定义，按逆序逐步消去便给 $Rg=1$。
反之若 $Rg=1$，可逐次消去 $R_i$，恢复该自然词的全部域。
因有界 $R_i$ 交换，任一排列给同一产品的值域；不能只检查各 $M_i1$ 分别有定义。

特别在秩二情形，
$$
\boxed{
1\in\operatorname{Ran}(R_1R_2)
\quad\Longleftrightarrow\quad
Cf_1\in\operatorname{Dom}M_2
\quad\Longleftrightarrow\quad
Cf_2\in\operatorname{Dom}M_1.
}
\tag{6.2}
$$
例如第一向：若 $R_1R_2g=1$，则
$R_2g=(M_1-\lambda_1)1=Cf_1-\lambda_1$，
所以 $Cf_1\in\operatorname{Dom}M_2$。
反向在此域条件下取
$g=(M_2-\lambda_2)(Cf_1-\lambda_1)$；
另一等价由交换 $1,2$ 的角色得到。
因此，一个真秩二湮灭者若两个最小乘子都有预解点，
就必须同时违反这两条交叉最小域条件。

如果除至多一个 $M_i$ 外其余全为有界乘子，而剩下一个有预解点，
则第一条件自动成立。其余 $R_i$ 是 $\mathfrak C$ 中的单位，
它们及其逆保持剩下乘子的域，而 $1$ 本来在该域中。
这给一个明确的有限秩排除类；不覆盖一般无界列族。

最后，改变各 $\lambda_i$ 不会自动消掉共同图缺陷。
预解恒等式给
$$
R_i(\lambda)
=R_i(\mu)
[I-(\lambda-\mu)R_i(\mu)]^{-1}.
$$
方括号及其逆是 $\mathfrak C$ 中的有界单位，二者都保持并双射于 $\Gamma$。
所以 (5.3) 的闭像 $\Gamma_R$ 不依赖选取哪个合法预解点。

## 7. 仍未证明的量词

秩一结论是对任何真湮灭向量的严格必要条件：
$X_{Cf}$ 必须有全复平面谱。全平面谱本身并不提供湮灭者。

有限秩情形仍可能出现：某个 $M_i$ 已无预解点，或者所有预解点都存在，
但共同图中有 (5.5) 所刻画的非零缺陷。
仅有正常性、有限秩、各自的稠密域及各自的预解式，
都没有在本文中排除这些情形。

R267 的普遍强单位和共同全部 $A$ 幂图核心不自动给 (6.1)，
也不自动给 $\Gamma_R=\Gamma$。指定慢主理想的全部正常见证、
未知子商稠密像以及普通 Hilbert ISP 仍开放。

## 已证依赖

- R244 §§1--3：最小闭乘子单端配对、正常右测试延拓及 $Sh=0$；本稿已全文重新核对。
- R34、R88：多项式共同图与有界强闭图交换；本稿第 1、5 节给出本次所需的具体极限证明。
- 全空间 $S_N,S_Y$ 单射性：仅用于从 $Sh=0$ 得 $h=0$；没有替换成未知限制或商上的单射性。
