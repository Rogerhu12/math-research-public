# R144：以三个真实 CM 点的高度差消去截面常数

日期：2026-11-12。**状态：已证明；全部 54 条校准方程及模 $47^4$ 的两侧逆附准确证书。** 本文把 R133 的绝对局部高度校准改为同一方向在两个真实点上的高度差。这样不需要先求 R54 的全局有理归一化乘数，也不需要选定一个绝对纤维标量。

仍必须构造实际拉回线丛在整条曲线上的代数平凡化，或其真实截面比；一个任意圆盘框架不能替代它。本文不宣称这些局部高度差已经算出。

## 1. 第三个实际 CM 点及其准确 Mordell–Weil 坐标

沿用 R89、R94、R133，令
$$
X=X_{\rm ns}^+(41),\quad J=\operatorname{Jac}(X),\quad
D=\text{全部20个尖点之和},\quad B=B_{-4}.
$$
两个已确定的有理 CM 点为 $P_{-3}$、$P_{-7}$，其 $j$ 值分别是 $0$、$-3375$；写
$$U_\delta=[20P_\delta-D]=r_\delta B\quad\text{于 }J(\mathbf Q)\otimes\mathbf Q.$$

### 引理 144.1

存在实际有理 CM 点 $P_{-12}$，其 $j=54000$，并且
$$
\boxed{T_2P_{-3}=3P_{-12},\qquad
U_{-12}=\frac13T_2U_{-3},\qquad r_{-12}=\frac13T_2r_{-3}.}
\tag{1.1}
$$

**证明。** 在 $j=0$ 曲线上取模型 $y^2=x^3+1$。三个非零二挠点的横坐标满足 $r^3=-1$；三阶 CM 自同构在它们上单传递。该自同构位于定义 $P_{-3}$ 的 CM Cartan 中，因而保持它的非分裂项链。于是三个真正二阶商连同传输的项链，在粗模曲线上给出同一个点，且每条同源都按对应的次数计入一次。这给第一式中的重数 $3$，不是把三个几何核当成三个不同有理点。

Vélu 商为
$$y^2=x^3-15r^2x+22.$$
因 $r^6=1$，其 $j$ 值准确为
$$1728\frac{4(-15r^2)^3}{4(-15r^2)^3+27\cdot22^2}=54000.$$
这是 CM 序判别式 $-12$ 的点。$T_2P_{-3}$ 定义于 $\mathbf Q$ 且仅支撑于该点，故该点本身有理。

全部尖点构成一个度 20 的 Galois 轨道；$T_2$ 定义于 $\mathbf Q$、保持尖点并有次数 $3$，所以 $T_2D=3D$。因此
$$T_2[20P_{-3}-D]=[60P_{-12}-3D]=3[20P_{-12}-D].$$
这证明其余两式。此处采用 R89 的实际带符号点坐标；没有重新挑选 Heegner 平方根。证毕。

## 2. 差值校准的完整矩阵

R94 的 53 个实际方向为
$$F_n=a_nT_n+b_n,\qquad G_n=2F_n,\qquad \eta_{D,G_n}=\xi_nB,$$
次序仍为 `p41_full_chow_heegner_certificate.json.gz` 中的 `indices[1:]`。这里 $G=2F$ 只取一次。

固定任意同一 Hecke 相容全局 Poincaré 高度；R140–R141 构造的相容局部对数也可使用。存在唯一 $s\in E\otimes\mathbf Q_{47}$，使
$$h(aB,bB)=\operatorname{Tr}(sab).$$
对任意已列 CM 点，R133 的准确向量为
$$v_{\delta,n}=2F_nr_\delta^2-r_\delta\xi_n.$$
令
$$
w_{\delta,n}=v_{\delta,n}-v_{-3,n}
=2F_n(r_\delta^2-r_{-3}^2)-(r_\delta-r_{-3})\xi_n.
\tag{2.1}
$$
则
$$
\boxed{h(U_\delta,G_nU_\delta-\eta_{D,G_n})
-h(U_{-3},G_nU_{-3}-\eta_{D,G_n})
=\operatorname{Tr}(s w_{\delta,n}).}
\tag{2.2}
$$

取准确的 54 行：

- 前 53 行取 $\delta=-12$，让 $n$ 遍历 R94 全部方向；
- 最后一行取 $\delta=-7,n=2$，此时 $F_2=27T_2+4$。

按 R89 的八域次序、各域使用 $1,H,\ldots,H^{d_f-1}$，令 $V_{\rm rel}$ 为这 54 个 $w$ 的行坐标矩阵，$G$ 为同一幂基的迹 Gram 矩阵。若 $\mathbf s$ 是 $s$ 的坐标列，$\mathbf L_{\rm rel}$ 为式 (2.2) 的高度差列，则
$$
\boxed{\mathbf L_{\rm rel}=M_{\rm rel}\mathbf s,
\qquad M_{\rm rel}=V_{\rm rel}G.}
\tag{2.3}
$$
程序由 R89 的真实 $r_{-3},r_{-7}$、R94 的真实 $T_2,F_n,\xi_n$ 逐域构造全部行；所有分母在 47 处为单位。准确结果为
$$
\boxed{\det V_{\rm rel}\equiv4,\quad
\det G\equiv46,\quad \det M_{\rm rel}\equiv43\pmod{47}.}
\tag{2.4}
$$
所以
$$
\boxed{\mathbf s=M_{\rm rel}^{-1}\mathbf L_{\rm rel}}
\tag{2.5}
$$
在 $\mathbf Z_{47}$ 上没有额外精度损失。证书包含模 $47^4$ 的完整 $V_{\rm rel},G,M_{\rm rel},M_{\rm rel}^{-1}$，并验证逆矩阵的两侧恒等式。式 (2.4) 同时证明前 53 行独立，最后一行准确补足缺失方向。

## 3. 从局部高度差得到右端，保持同一个坏分量

令 $\widetilde s_n$ 为 R54 的真实全局归一化截面。实际坏高度分量标号为
$$
j(P_{-3})\equiv0,\qquad j(P_{-12})\equiv3,\qquad
j(P_{-7})\equiv28\pmod{41}.
$$
以 $0$ 为参考，R54 给
$$h(U_\delta,G_nU_\delta-\eta_{D,G_n})
=\lambda_{47}(\widetilde s_n(P_\delta))
-\log_{47}(41)b_{i_\delta}(F_n).$$
因此首 53 行的准确右端是
$$
\boxed{L_{{\rm rel},n}=
\lambda_{47}(\widetilde s_n(P_{-12}))
-\lambda_{47}(\widetilde s_n(P_{-3}))
-\log_{47}(41)b_3(F_n).}
\tag{3.1}
$$
最后一行是
$$
\boxed{L_{{\rm rel},54}=
\lambda_{47}(\widetilde s_2(P_{-7}))
-\lambda_{47}(\widetilde s_2(P_{-3})),}
\tag{3.2}
$$
因为 R134 已证明 $b_{28}(27T_2+4)=0$。R135 的完整坏谱提供式 (3.1) 的全部 $b_3(F_n)$；它们已逐行写入本证书。没有把前 53 行各自挑一个不同的坏靶。

## 4. 为什么不必计算绝对全局归一化常数

取 R54 同一个实际拉回线丛 $\mathscr L_n$。它在整条泛纤维曲线上可平凡化。若为处理有理方向先清分母、取固定整张量幂，则以下论证对该幂作完再除以同一倍数，不能改变前文的 $G=2F$ 规范。若该张量幂含47因子，实际高度差须相应提高输入精度；式 (2.4) 仅保证校准矩阵本身不再损失精度。

在 $X_{\mathbf Q_{47}}$ 上选任意实际的**全局无零极代数截面** $t_n$。因曲线完整且几何连通，两个这样的全局截面的比必为常数，所以
$$t_n=c_n\widetilde s_n,\qquad c_n\in\mathbf Q_{47}^{\times}.$$
这里允许 $c_n$ 不是有理数；不必计算它。Poincaré 对数的纤维规律立即给
$$
\begin{aligned}
&\lambda_{47}(t_n(P))-\lambda_{47}(t_n(P_{-3}))\\
&\hspace{10mm}=\lambda_{47}(\widetilde s_n(P))
-\lambda_{47}(\widetilde s_n(P_{-3})).
\end{aligned}
\tag{4.1}
$$
所以式 (3.1)、(3.2) 可全部改用 $t_n$。R54 为消去其他素数垂直阶而引入的有限有理乘积，以及坏素数参考分量的共同倍率，都在差值中准确相消。

可以直接计算 $t_n(P)$ 与 $t_n(P_{-3})$ 的真实纤维比，而不先指定某个绝对标量。不同方向可以分别选全局平凡化；相对于真实可加截面族的常数在各自差值中相消，所以得到的方向泛函仍一致。

**精确边界。** 若只在一个圆盘上任意挑分析框架，它与 $\widetilde s_n$ 的比可以是随点变化的函数；这时式 (4.1) 不成立。即使局部 Poincaré 对数和 Hecke 修正已知，仍须构造该全局代数截面，或给出等价的规范双扩张/对应截面比。本文消去的是常数归一化工作，没有消去真实截面本身。

## 5. 完整 QC 缺陷没有改变

在 R121 的真实积分对数坐标中，将 $\log U_x$ 写成 $r(x)\log B$，并设
$$v_n(x)=2F_nr(x)^2-r(x)\xi_n.$$
定义
$$
\mathcal Q^{\rm rel}_{F_n}(x)
=\operatorname{Tr}(s[v_n(x)-v_{-3,n}])
-\left[\lambda_{47}(t_n(x))-\lambda_{47}(t_n(P_{-3}))\right].
\tag{5.1}
$$
由式 (4.1)，它等于 R54 的原缺陷 $\mathcal Q_{F_n}(x)$ 减去 $\mathcal Q_{F_n}(P_{-3})$。后者为零，因为 $P_{-3}$ 是参考坏分量上的真实有理点。因此
$$\boxed{\mathcal Q^{\rm rel}_{F_n}(x)=\mathcal Q_{F_n}(x).}\tag{5.2}$$

故全部圆盘上的共同根、R135 的同一四个联合坏靶，以及 R140 的相容 splitting 不变性均完整保留。该差值方法没有改变待解的 QC 问题。

### 5.1 将差值准确化为以 $P_{-3}$ 为基点的全局截面

这一步给出实际截面构造可直接使用的输入，而不只是在数值高度中相减。置
$$b=P_{-3},\quad d=20,\quad x(P)=[P-b],\quad U_b=[db-D],$$
并暂省去方向下标，写 $G=2F$、$\eta=\eta_{D,G}$。原拉回线丛的纤维是
$$\mathscr L(P)=\mathcal P_{dx(P)+U_b,\,dGx(P)+GU_b-\eta}.$$
令 $\mathscr L(b)^{-1}$ 表示将一个固定一维向量空间的对偶拉回到整条曲线上。则有保持 $b$ 处刚性化的全局线丛同构
$$
\boxed{\mathscr L\otimes\mathscr L(b)^{-1}
\simeq x^*(\mathrm{id},G_b\mathrm{id}-\eta_b)^*\mathcal P,
\quad G_b=d^2G=2d^2F,\quad
\eta_b=d\eta-2dGU_b=d\eta-4dFU_b.}
\tag{5.3}
$$

**证明。** 在任意基变换上使用 Poincaré 双扩张的两条分配律，左边在 $P$ 的纤维准确分为
$$
\mathcal P_{dx,dGx}\otimes
\mathcal P_{dx,GU_b-\eta}\otimes
\mathcal P_{U_b,dGx}.
$$
被除掉的第四项恰是固定纤维 $\mathcal P_{U_b,GU_b-\eta}$。因为 $G$ Rosati 自伴随，真实的对称同构及 $G$ 的规范伴随同构将第三项识别为 $\mathcal P_{x,dGU_b}$；第一、二项分别识别为 $\mathcal P_{x,d^2Gx}$ 和 $\mathcal P_{x,d(GU_b-\eta)}$。再用第二条群律合并即得 (5.3)。每个同构来自双扩张自身，故在 $x=0$ 都保持规范单位，且在整条曲线上代数地相容。这没有把不同纤维的标量直接相除。若 $G,\eta$ 为有理方向，则先取同一个清分母张量幂，证明完全相同。证毕。

由 (5.3)，任一全局无零极截面 $t$ 给出新线丛上在 $b$ 取值为 $1$ 的截面
$$t_b(P)=\operatorname{image}\bigl(t(P)\otimes t(b)^{-1}\bigr).$$
它与 $t$ 的常数倍选择无关，且是新线丛上满足该刚性化的唯一全局无零极截面：两者之比是完整几何连通曲线上的常数，在 $b$ 为 $1$。因此可以从真实对应直接构造这个以 $b$ 为基点的截面，无须先计算原截面的绝对常数。

同一个 Hecke 相容、对称 Poincaré 对数保持上述全部同构，故
$$
\lambda_{47}(t_b(P))=
\lambda_{47}(t(P))-\lambda_{47}(t(b)).
\tag{5.4}
$$
其全局双线性值也准确为
$$
h(x,G_bx-\eta_b)
=h(U_P,GU_P-\eta)-h(U_b,GU_b-\eta).
\tag{5.5}
$$
在 $x(P_\delta)=(r_\delta-r_{-3})B/d$ 上展开右边即为 (2.1)，因此不会另引一个 $d^2$ 倍率或丢失线性平移。

已发表的 [Edixhoven–Lido, *Geometric quadratic Chabauty*, §7，尤其命题7.2、7.5、7.8](https://doi.org/10.1017/S1474748021000244) 给出这种以 $b$ 刚性化的对应线丛和对角截面的代数描述；本节已直接证明将它接到本题实际 $u_D,G,\eta$ 的全部转换。数值实现仍须构造对应、取真实范数并处理对应与对角或 $b$ 的交点；在 $P_{-12}\in T_2(b)$ 处不能以未消去的零值代替局部方程、切向单位与相应的线丛刚性化。

## 6. 源码与最终证书

源码：`scripts/p41_cm_relative_calibration47.py`；复用 R133 生成器中的准确有限环矩阵乘法和单位主元逆，不使用浮点。

证书：`scripts/data/p41_cm_relative_calibration47_certificate.json.gz`。它保存 54 个准确点/方向标签、完整矩阵及逆、$r_{-12}$ 的 47 进坐标、53 个同一坏分量的高度差、所有来源哈希。文件为 35500 字节，SHA256：

`c8904bfcf4f0f2c77b84f7477c3b71e70b2bcec556943f55f65f0f00ab593b12`。

在课题目录复算：

```bash
python scripts/p41_cm_relative_calibration47.py
```

数学依赖均为已经识别的实际输入：R54 的全局截面和同一坏分量规范；R89 的带符号 CM 坐标；R94 的全部真实对应和平移；R133 的迹 Gram 及高度规范；R134–R135 的完整坏项；R140–R141 的相容局部对数接口。引理 144.1 的实际二同源关系、差值不变性及新的可逆校准在本文中直接证明。
