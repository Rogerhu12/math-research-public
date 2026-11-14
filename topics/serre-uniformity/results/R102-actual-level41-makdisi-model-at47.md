# R102. 层 41 在辅助素数 47 处的实际 Makdisi 评价模型

日期：2026-11-12；qc_global。**状态：已证明，附模 $47^4$ 的完整评价矩阵及精确有限算术证书。**

令 $X=X_{\rm ns}^+(41)$，$D$ 为全部尖点之和。本文构造真实曲线 $X$ 的如下数据：
$$
g=54,\quad \deg D=20,\quad
\mathcal L=\mathcal O_X(K_X+D),\quad \deg\mathcal L=126,
$$
以及在同一非椭圆纤维中的 $820$ 个点上，$H^0(X,\mathcal L)$ 的 $73$ 元整基的评价矩阵。全部评价在
$$
\boxed{R_2=(\mathbb Z/47^4\mathbb Z)[i]/(i^2+1)}
\tag{0.1}
$$
中给出，包含实际 Frobenius 置换、基的半线性下降矩阵和准确局部 $L$ 因子。构造不假定权一乘积在特征 $47$ 自动生成；实际 $73$ 阶子式为
$$
\boxed{43+17i\pmod{47},\qquad
\operatorname{Norm}(43+17i)=23\ne0\pmod{47}.}
\tag{0.2}
$$

R94 已完成全部全局 Chow–Heegner 平移。本文给出下一项真实局部计算对象；它尚不包含 Poincaré 局部高度函数、QC 共同根或 Serre 一致性的结论。

## 1. 所用实际曲线、域与评价点

固定
$$E_0:\ y^2=x^3+x+32,\qquad j(E_0)=1728/6913\equiv9\pmod{47}.$$
它在 $47$ 好约化，实际点数和为 $48$，所以约化 Frobenius 的迹是零。其在 $E_0[41]$ 上的矩阵可取
$$F=\begin{pmatrix}0&35\\1&0\end{pmatrix},\qquad F^2=35I\pmod{41}.$$
$35=-47\pmod{41}$ 的阶为 $40$，且 $X^2-35$ 在 $\mathbb F_{41}$ 不可约。因此 $F$ 的准确阶为 $80$，$F^{40}=-I$。

前置数据 `scripts/data/p41_local47_torsion_certificate.json` 给出一个不可约 $80$ 次多项式 $f$、环
$$R_{80}=(\mathbb Z/47^4\mathbb Z)[t]/\widetilde f(t),$$
以及 $E_0(R_{80})$ 中的实际基 $P,Q$，满足
$$[41]P=[41]Q=0,\quad \varphi(P)=Q,\quad
\varphi(Q)=[-47]P.$$
这里 $\varphi$ 是由 $f(\varphi(t))=0$ 和 $\varphi(t)\equiv t^{47}\pmod{47}$ 唯一确定的未分歧 Frobenius。实际 Miller 算法证明
$$\zeta=e_{41}(P,Q)$$
是本原 $41$ 次单位根；该证书不是只保存一个抽象共轭类。独立复核器同时验证不可约性、曲线方程、群律、配对和 Frobenius。

因为 $47$ 在 $(\mathbb Z/41\mathbb Z)^\times$ 中的阶为 $40$，
$$K=\mathbb Q_{47}(\zeta)$$
是未分歧 $40$ 次扩张。令 $L/\mathbb Q_{47}$ 为其二次未分歧子扩张，用 $i^2=-1$ 表示。程序保存 $i$ 在 $R_{80}$ 中的实际坐标，并检验 $\varphi(i)=-i$。符号以其模 $47$ 多项式表示的第一个非零系数位于 $\{1,\ldots,23\}$ 唯一固定。

采用 R94 的全部项链标号
$$
R_{a,e}=\begin{pmatrix}a&e-a^2\\1&-a\end{pmatrix},
\qquad a\in\mathbb F_{41},\quad \left(\frac e{41}\right)=-1.
\tag{1.1}
$$
共有 $41\cdot20=820$ 个。每个标号与实际基 $(P,Q)$ 结合，给 $E_0$ 上的一个真实无定向项链。由于 $j(E_0)\not\equiv0,1728\pmod{47}$，这些点在粗模曲线上有不同的约化，均位于 $X\to X(1)$ 的非分歧纤维。

$F^2$ 为标量，故这 $820$ 个模曲线点均在 $L$ 定义；完整挠点基需要 $80$ 次扩张并不迫使模曲线点也需要该扩张。对每个 (1.1)，直接计算 $FR_{a,e}F^{-1}$，把左下角归一化为一，得到保存的 Frobenius 置换 $\tau$。它有 $22$ 个不动点和 $399$ 个二循环，且 $\tau^2=1$。所有标号、代表矩阵及置换均在证书中。

短 Weierstrass 方程的 $dx/(2y)$ 在这些非椭圆点给权二形式的局部评价规范。经 Kodaira–Spencer 同构，权二形式的空间是 $H^0(X,K_X+D)$；在椭圆点处须处理粗模参数，但本评价纤维没有该问题。

## 2. 权一形式的实际有限环求值

对非零 $41$ 挠点 $T$，记 $e(T)$ 为 moduli-friendly 权一 Eisenstein 形式的值。所用精确关系是
$$
e(T)+e(U)-e(T+U)=\lambda(T,U),\qquad e(-T)=-e(T),
\tag{2.1}
$$
其中 $T,U,T+U\ne0$，$\lambda$ 为连线斜率，$T=U$ 时取切线斜率。这是 Khuri-Makdisi 的模解释；参见 Mascot (2022)，Theorem 4.1.2 的第一项及 Proposition 4.3.1。本文只使用形式的存在、整性与 (2.1)，不援用其特征 $47$ 生成性。

沿循环群逐次应用 (2.1)，得到
$$e([m]P)=m e(P)-\sum_{k=1}^{m-1}\lambda(P,[k]P).$$
在 $m=40$ 处用 $[40]P=-P$，故
$$
\boxed{e(P)=\frac1{41}\sum_{k=1}^{39}\lambda(P,[k]P).}
\tag{2.2}
$$
$Q$ 同理，再由
$$e([a]P+[b]Q)=e([a]P)+e([b]Q)-\lambda([a]P,[b]Q)$$
计算全部 $1680$ 个值。

所有除法在 $R_{80}$ 中都有单位分母。轴上的弦斜率排除了 $[k]P=\pm P$ 的非切线情形；切线分母 $2y(P)$ 不为零，因为一个 $41$ 阶点不可能为二阶点。两条轴之间，$x([a]P)=x([b]Q)$ 会推出 $[a]P=\pm[b]Q$，与基的独立性矛盾。这些判断已在剩余域成立，所以分母在整个未分歧环中为单位。$41$ 也是单位。

生成器采用批量求逆；唯一总逆先在剩余域求出，再用 $b\leftarrow b(2-ab)$ 提升。复核器用同样的代数恒等式、独立的标准库多项式运算重建全部值。不会对含零因子的复合模数多项式环盲目使用域除法。

这些形式在 $47$ 处整且在尖点全纯：其模解释在 $6\cdot41$ 可逆的基上成立；等价地，标准 $q$ 展开只出现此处为单位的 $41$ 和 $1-\zeta^a$ 分母。因此以下有限和确实给出整的全局权二截面。

## 3. 准确的正规化子与二次域下降

令 $H_1$ 是 $\mathrm{SL}_2(\mathbb F_{41})$ 中 $F$ 的射影正规化子。它由
$$
\begin{pmatrix}a&35b\\b&a\end{pmatrix},\quad a^2-35b^2=1,
\qquad
\begin{pmatrix}a&-35b\\b&-a\end{pmatrix},\quad a^2-35b^2=-1
\tag{3.1}
$$
组成，阶为 $84$。程序取 $H_1/\{\pm I\}$ 的全部 $42$ 个代表；两个权一形式的乘积对符号不变。

对每个 (1.1)，选择 $s^2=e/35$ 及满足
$$\det g_{a,e}=1,\qquad g_{a,e}F g_{a,e}^{-1}=R_{a,e}/s$$
的实际矩阵 $g_{a,e}$。可以令 $w^2-ec^2=s$、$v=w+ac$，取
$$g_{a,e}=\begin{pmatrix}
v&(av+(e-a^2)c)/s\\ c&(v-ac)/s
\end{pmatrix}.$$
非分裂二元范数取遍所有非零值，故这样的选择存在；程序还直接验证每个矩阵的两个等式。

对非零向量 $v,w\in\mathbb F_{41}^2$，令
$$B_{v,w}=\sum_{h\in H_1/\{\pm1\}}f_1^{hv}f_1^{hw}.$$
这是定义于 $K$ 的真实权二形式。它在项链 $(a,e)$ 上的值是
$$B_{v,w}(a,e)=\sum_h e(\beta g_{a,e}hv)e(\beta g_{a,e}hw),\qquad \beta(1,0)=P,\quad\beta(0,1)=Q.$$

本文使用下降截面
$$
\boxed{\Psi_{v,w}=\operatorname{Tr}_{K/L}(\zeta B_{v,w}).}
\tag{3.2}
$$
这是截面的 Galois 迹，故是 $L$ 上的整权二截面。评价点和其局部规范均在 $L$ 定义，所以 (3.2) 的评价等于其数值的域迹。这里的 $\zeta$ 是先前的真正 Weil 配对，不是另选一个没有和层结构对应的根。

原始乘积的数值在 $K$ 中：$\varphi^{40}$ 在实际 $41$ 挠点上为 $-1$，由 (2.1) 的奇性，两个权一值的乘积被 $\varphi^{40}$ 固定。$\zeta$ 同样在该子域。因此 (3.2) 可直接从 $80$ 次环中的值准确计算。

具体随机种子41047只用于列出100对候选 $(v,w)$；证书完整保存了这些向量和选出的73对。随机性不进入证明，因为最后的单位子式为精确有限算术证据。未加 $\zeta$ 的同一相对迹在此次候选集上仅有秩37；实际选取 (3.2) 不是把未核验的生成性当成输入。

## 4. 迹双线性矩阵使高精度计算保持紧凑

若 $z\in\mathcal O_K/47^4$，写
$$\operatorname{Tr}_{K/L}(z)=A+Bi.$$
因为 $[\mathcal O_{80}:\mathcal O_K]=2$，有
$$
\boxed{A=\tfrac14\operatorname{Tr}_{80/1}(z),\qquad
B=-\tfrac14\operatorname{Tr}_{80/1}(iz).}
\tag{4.1}
$$
这同时证明二次域表示和归一化系数 $1/4$，没有遗漏两倍的绝对迹。

取全部非零挠点向量模 $\pm1$ 的840个代表，把各 $e_u$ 在多项式基 $1,t,\ldots,t^{79}$ 下的坐标写成矩阵 $E$。定义两个 $80\times80$ 的 Hankel 矩阵
$$
(H_0)_{ab}=\tfrac14\operatorname{Tr}_{80/1}(\zeta t^{a+b}),\qquad
(H_1)_{ab}=-\tfrac14\operatorname{Tr}_{80/1}(i\zeta t^{a+b}),\quad0\le a,b<80.
$$
则
$$E^{\mathsf T}H_0E,\qquad E^{\mathsf T}H_1E$$
恰给全部 $\operatorname{Tr}_{K/L}(\zeta e_u e_v)$ 的实部与 $i$ 系数。恢复正负向量只须乘相应符号，再按 (3.1) 的42项求和。

生成器用 PARI 的有限环矩阵乘法；标准库复核器从 $f$ 的 Newton 和独立重建 $\operatorname{Tr}(t^n)$，再进行整数模矩阵乘法。整个步骤没有浮点数、精度猜测或数值识别。

## 5. 完整整基与 Frobenius 的证书

令 $M$ 为 (3.2) 的 $820\times100$ 实际评价矩阵。其模 $47$ 的秩为73。保存的列集 $J$、行集 $I$ 均有73个元素，且
$$\det M_{I,J}=43+17i\pmod{47}.$$
该值的范数为23，故矩阵 $P=M_{I,J}$ 在 $R_2$ 上可逆。

设 $V=M_{*,J}$、$C=P^{-1}$，并取
$$W=VC.$$
证书保存完整 $C$ 和 $W$，满足
$$PC=1,\qquad W_{I,*}=1\pmod{47^4}.$$
逆矩阵先在 $\mathbb F_{47^2}$ 求出，然后以矩阵 Newton 公式提升，最后直接相乘核验。

这已经证明所选截面是完整整基。事实上 $X$ 在47有光滑好模型，尖点除子在此处也为 étale；$\deg(K_X+D)=126>2g-2=106$，所以 $H^1(K_X+D)=0$，其整截面模为秩
$$126+1-54=73$$
的自由模并与约化交换。上述73个整截面模47独立，由 Nakayama 引理构成整个整截面模的基。无需另加“权一形式模47生成”假设。

令 $\sigma(i)=-i$。Frobenius 对截面的评价矩阵是
$$Y_{n,k}=\sigma(W_{\tau(n),k}).$$
取 $A=Y_{I,*}$，证书在 $R_2$ 中逐项验证
$$
\boxed{WA=Y,\qquad A\sigma(A)=1.}
\tag{5.1}
$$
因此这里既有实际点的 Frobenius 置换，也有完整评价空间的半线性下降；不是只从维数推测其稳定性。

## 6. 实际局部因子及 Makdisi 条件

R94 保存了完整实际 Hecke 代数的八个数域及每域中的 $a_{47,f}$。程序从这些准确有理域坐标计算
$$
P_{47}(T)=\prod_f\operatorname{Norm}_{E_f/\mathbb Q}(T^2-a_{47,f}T+47).
\tag{6.1}
$$
所得整系数首一多项式次数108，$T^{107}$ 系数为81，常数项为 $47^{54}$，满足准确功能方程。全部109个系数保存在证书。标准库复核器通过各域的幂和与 Newton 恒等式独立重算 (6.1)，不是再次调用生成器的 resultant。

特别是 $\#X(\mathbb F_{47})=47+1+81=129$，与独立残差圆盘盘点一致；该总数不等于当前选定一个 $j$ 纤维中的22个有理评价点。

最后，
$$\deg\mathcal L=126\ge2g+1=109,\qquad820>5\deg\mathcal L=630.$$
因此这些相异的评价点分离 $\mathcal L^{\otimes n}$ 的截面，$n\le5$；正次数线丛的正常生成性使所需乘积空间可从 $W$ 重建。各空间的维数为
$$73,\quad199,\quad325,\quad451,\quad577.$$
这正满足 Mascot (2022)，Definition 3.1.1 与 Remark 3.1.4 的有限精度 Makdisi 模型条件。本文给的是模 $47^4$ 的实际模型。固定 $E_0$、实际挠点剩余基、(3.2) 的截面及评价规范后，étale 挠点提升和单位矩阵求逆唯一确定这里的兼容提升；这不表示任意模 $47^4$ 截面都有唯一提升，也不是只在特征47中偶然匹配的矩阵。

## 7. 文件、复算与用途

- 生成器：`scripts/p41_makdisi47.py`、`scripts/p41_makdisi47.gp`。
- 完整标准库复核：`scripts/verify_p41_makdisi47.py`。
- 数据：`scripts/data/p41_makdisi47_certificate.json.gz`，压缩521301字节，原JSON1193612字节。
- SHA256：`c6ea2f89f4f64eec78039c5b14b6835295b045ea24ae26f885c4047b21e96222`。

在课题目录运行：

```
python -B scripts/p41_makdisi47.py --gp /tmp/pari-2.19.0/gp
python -B scripts/verify_p41_makdisi47.py
```

生成器使用 PARI/GP 2.19.0，约一分钟完成。它引用的挠点证书和 R94 证书的文件哈希均写入输出；不保存大中间矩阵。单靠本证书尚不能计算全部 QC 根。继续的实际任务是把 CM 点及其粗模局部参数送入这个模型，再计算 R94 对应的 Poincaré 截面和局部高度。

### 原始文献

1. K. Khuri-Makdisi，*Moduli interpretation of Eisenstein series*，International Journal of Number Theory **8** (2012)，715–748；尤其权一形式的代数构造及 Corollary 3.13。[作者全文](https://arxiv.org/pdf/0903.1439)。其完整生成定理在特征零证明，本文以实际单位子式处理特征47。
2. N. Mascot，*Moduli-friendly Eisenstein series over the p-adics and the computation of modular Galois representations*，Research in Number Theory **8** (2022)，Article 48；Definition 3.1.1、Remark 3.1.4、Theorem 4.1.2 的模解释、Proposition 4.3.1、§4.4。[已发表全文](https://doi.org/10.1007/s40993-022-00329-6)。
