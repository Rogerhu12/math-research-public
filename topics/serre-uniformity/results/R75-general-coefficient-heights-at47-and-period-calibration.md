# R75. 层 41 的一般系数域高度公式与周期校准

日期：2026-11-12。会话：serre-uniformity-resume2；根会话。

**状态：已证明。** 本文补上 R74 选定辅助素数 $47$ 后的系数域接口：无需假设 $47$ 在所有 Hecke 系数域完全分裂，已发表的普通 $\ell$ 进 Gross–Zagier 定理仍给出真实 Heegner 自高度及 R68 的极化传输公式。另将圆分 Rankin 导数写成两个普通模形式 $L$ 函数的乘积导数，保留准确周期因子；因此只要实际计算普通圆分导数，就能判定各高度是否为零。

这里没有把“在另一素数成立的公式”跨素数延拓。所用一般系数域输入是 Disegni (2015) 的**期刊版本** Theorems A、B、§4.4 和 Proposition 6.3.1；不是其 2017 年论文中后来更正过的常数公式。

## 1. 实际数据与记号

令
$$N=41^2,\qquad J_0=J_0(N),\qquad
J=J_{\rm ns}^+(41).$$
沿用 R57、R68、R71、R74：$J$ 的全部 $54$ 维均为实际解析秩一 Heegner 部分。其归一化新形式为 $\mathcal F_{41}$，全部取 new、Fricke $+$，不能与模符号的星号混淆。

对每个 Hecke 轨道 $f$，记系数域为 $E_f$。固定任一嵌入
$$\sigma:E_f\hookrightarrow\overline{\mathbb Q}_{47}.$$
R74 已从真实 $T_{47}$ 矩阵证明 $\sigma(a_{47})$ 为单位，故
$$X^2-\sigma(a_{47})X+47$$
有唯一单位根 $\alpha_{f,\sigma}$。它属于包含 $\sigma(E_f)$ 的一个有限扩张 $L/\mathbb Q_{47}$。置
$$U_{f,\sigma}=1-\alpha_{f,\sigma}^{-1},\qquad
E_{f,\sigma}=\frac{48-\sigma(a_{47})}{47}.$$
这两个量都非零：若 $\alpha=1$，则 $\sigma(a_{47})=48$；代数嵌入单射会使 $a_{47}=48$，与任一复嵌入的 Weil 界 $|a_{47}|\le2\sqrt{47}$ 矛盾。$E$ 的非零性相同。

分别取
$$D\in\{-43,-163\},\qquad K_D=\mathbb Q(\sqrt D),\qquad
g_D=f\otimes\chi_D.$$
两个域都是类数一，单位仅为 $\{\pm1\}$，$41$ 和 $47$ 都分裂。R74 给每个共轭 $L(g_D,1)\ne0$。记所选定向 Heegner 点为 $P_D\in X_0(N)(K_D)$，并置
$$y_f^{(D)}=e_f[P_D-\infty].$$
在 $J_0(K_D)\otimes\mathbb Q$ 中它位于有理子空间且非挠；投影到 $\sigma$ 的记号加下标 $\sigma$。

固定一个普通圆分方向 $\nu$ 及其对数 $\ell_{\mathbb Q}=\log\nu$。在 $K_D$ 上使用
$$W_D=\nu\circ N_{K_D/\mathbb Q},\qquad
\ell_{K_D}=\ell_{\mathbb Q}\circ N_{K_D/\mathbb Q}.$$
高度在 $47$ 处用单位根 Hodge splitting，其他地方按同一全球对数定义。下文的圆分导数与高度**始终使用同一个 $\nu$**。若改用反向 Artin 约定，必须同时把两边的对数变号。

## 2. 一般系数域的已发表定理确实适用

Disegni (2015) 在 Theorem A 之前直接令 $L$ 为 Fourier 系数与普通单位根生成的有限 $\mathbb Q_\ell$ 扩张。Theorem B 并没有要求 Hecke 系数域完全分裂。其全实基域记为 $F$，CM 域记为 $E$；本题代入
$$F=\mathbb Q,\quad E=K_D,\quad \ell=47,\quad N=1681.$$
逐项条件如下：

| 原定理条件 | 本题验证 |
|---|---|
| 权二、本原、平凡中心特征 | $f\in\mathcal F_{41}$ 的定义 |
| $\ell\nmid2N$、在所选嵌入普通 | R74 的真实 $T_{47}$ 证书 |
| CM 判别式与 $N\ell$ 互素且为奇数 | $D=-43,-163$ |
| $F$ 中 $\ell$ 上方素理想主且在 $E$ 分裂 | $F=\mathbb Q$；R74 的二次剩余计算 |
| $\chi_D(N)=(-1)^{[F:\mathbb Q]-1}$ | 两边均为 $1$ |

原定理的 $D_F^{-2}$ 因子是 $1$；两个局部 Euler 平方因子因为 $\chi_D(47)=1$ 合成 $U_{f,\sigma}^4$。这给出
$$C_{f,\sigma}^{(D)}
:=\left.\frac{d}{ds}\right|_{s=0}
\mathscr L_{47}^{\rm Dis}(f^\sigma/K_D,W_D^s)
=U_{f,\sigma}^4\,h_{K_D,\sigma}(z_f^{(D)},z_f^{(D)}).
\tag{2.1}$$
其中 $\mathscr L^{\rm Dis}$ **固定为该文 Theorem A 的 Rankin 规范**。没有把某个软件采用的任意周期规范直接当成这个函数。

## 3. Hodge 基点、单位因子和从 $K_D$ 到 $\mathbb Q$ 的二倍

原文的 Heegner 类为
$$z=u^{-1}\bigl(\operatorname{Tr}_{H/K_D}P_D-h[\xi]\bigr),$$
其中 $\xi$ 是度一 Hodge 类，$u=[\mathcal O_{K_D}^{\times}:\mathbb Z^\times]$。本题 $H=K_D$、$h=1$、$u=1$。还须证明 $[\xi]$ 可以替换成 $[\infty]$，不能凭“都是度一”替换。

### 引理 1

在 $\operatorname{Pic}^1(X_0(N))\otimes\mathbb Q$ 中，$[\xi]=[\infty]$；故原定理的 $z_f^{(D)}$ 就是上述 $y_f^{(D)}$。

**证明。** 已发表 Proposition 6.3.1(3) 给 $T_2[\xi]=3[\xi]$。标准 Hecke 尖点计算也给 $T_2[\infty]=3[\infty]$，因为 $2\nmid N$。于是度零类 $v=[\xi-\infty]$ 满足 $(T_2-3)v=0$。

在 $J_0(N)$ 的特征零分解中，$T_2$ 的全部特征值都来自权二尖形式，绝对值至多 $2\sqrt2<3$；旧形式也服从同一界，因为 $2$ 不除水平。故 $T_2-3$ 是一个同源，在 $J_0(\overline{\mathbb Q})\otimes\mathbb Q$ 上可逆。于是 $v=0$。这也说明实际未张量的差只有挠点影响，任何本题双线性高度与对数均杀掉它。证毕。

高度采用各地方求和的全球定义。对从 $\mathbb Q$ 基变换的点，原文 Proposition 5.1.2(5) 的局部范数相容性给
$$h_{K_D,\sigma}(y,y)=2h_{\mathbb Q,\sigma}(y,y).
\tag{3.1}$$
确切地，各个 $\mathbb Q$ 地方上方的局部度之和为 $2$；取 $\ell_{K_D}=\ell_{\mathbb Q}\circ N$ 后，相应局部高度也按这个局部度相加。$47$ 分裂时，两份局部项分别等于有理局部项。不能在定义中先除 $[K_D:\mathbb Q]$，再沿用 (3.1)。

因此 (2.1) 在实际 Heegner 向量上成为
$$\boxed{\quad
h_{\mathbb Q,\sigma}(y_f^{(D)},y_f^{(D)})
=\frac{C_{f,\sigma}^{(D)}}{2U_{f,\sigma}^4}.
\quad}\tag{3.2}$$
这个 $1/2$ 来自真实基变换次数。它与另一篇论文中因导数参数约定产生、后来更正的常数问题不能混为一谈。

## 4. 准确接入实际项链同源和微分坐标

取 R71 的真实同源 $q=\phi r$。在相应实际因子上写
$$q q^\dagger=\kappa_f,\qquad
q^*\omega_{J,f,\sigma}=a_{f,\sigma}\omega_{0,f,\sigma}.$$
这不是把一个抽象 Jacquet–Langlands 同构自行当成保持主极化的同构。

将 $P_f=m_f qy_f^{(D)}$ 作为 R68 的有理 Mordell–Weil 基向量；$m_f$ 清除投影分母并使其为实际点。极化高度的伴随相容性给
$$\boxed{\quad
\sigma(c_f)
=m_f^2\sigma(\kappa_f)
\frac{C_{f,\sigma}^{(D)}}{2U_{f,\sigma}^4}.
\quad}\tag{4.1}$$
这里 $c_f$ 是相对于该**点基**的系数。若用微分对数坐标拟合高度，令
$$u_{f,\sigma}^{(D)}=
\log_{\omega_{0,f,\sigma}}y_f^{(D)},\qquad
B_{f,\sigma}^{(D)}=E_{f,\sigma}^2
\bigl(u_{f,\sigma}^{(D)}\bigr)^2,$$
则 R68 的一般系数嵌入 BDP 公式及 R74 的非挠性给 $B_{f,\sigma}^{(D)}\ne0$，并有
$$\boxed{\quad
\gamma_{J,f,\sigma}
=\frac{\sigma(\kappa_f)}{2a_{f,\sigma}^2}
\frac{C_{f,\sigma}^{(D)}U_{f,\sigma}^{-4}}
{B_{f,\sigma}^{(D)}E_{f,\sigma}^{-2}}.
\quad}\tag{4.2}$$
$m_f^2$ 在点高度与对数平方的比中消去。R71 已算出 $\kappa$ 的行列式素因子仅为 $2,3,5,113,461$，所以 $47$ 处存在所列实际同源的整右逆；该整性不替代 $a_{f,\sigma}$ 的真实选择。

式 (4.1)–(4.2) 在任意有限系数扩张中成立。先扩大 $L$ 分解 Hecke 幂等元只是忠实的标量扩张，不会要求底域 $\mathbb Q_{47}$ 已含全部特征值。

## 5. 圆分 Rankin 导数的周期校准

选用原文 §4.4 的普通单变量 $L$ 函数及其非零 Shimura 周期 $\Omega_f^+$、$\Omega_{g_D}^+$。记
$$\Omega_f=8\pi^2\langle f,f\rangle_N,\qquad
\mathcal P_{f,D}
=\frac{\Omega_f^+\Omega_{g_D}^+}{|D|^{-1/2}\Omega_f}.
\tag{5.1}$$
原文的周期相容性使 $\mathcal P_{f,D}$ 为非零代数数；这允许在所选 $47$ 进嵌入下比较它，不允许把它未经计算置为 $1$。

**期刊版本**的 (4.4.1) 保留字符因子，给
$$\mathscr L_{47}^{\rm Dis}(f/K_D,\chi\circ N)
=\chi(|D|)^2\mathcal P_{f,D}
L_{47}(f,\chi)L_{47}(g_D,\chi).
\tag{5.2}$$
作者早期网页版本在该位置没有写这个字符因子；本题采用期刊版。下面的中心一阶导数仍可简化，但理由须明确写出。

因为 $w_N(f)=+1$，权二复函数方程符号为 $-1$，故 $L(f,1)=0$。普通插值遂给 $L_{47}(f,1)=0$。把 $\chi=\nu^s$ 代入 (5.2) 并求导：字符因子的导数项和 $g_D$ 因子的导数项都乘 $L_{47}(f,1)$，因而为零。因此
$$\boxed{\quad
C_{f,\sigma}^{(D)}
=\sigma(\mathcal P_{f,D})\,
L'_{47,\nu}(f^\sigma,1)\,
L_{47}(g_D^\sigma,1).
\quad}\tag{5.3}$$
导数是 $d/ds|_{s=0}$，与 (2.1) 的 $W_D^s=(\nu^s)\circ N$ 完全相同，没有另加一个 $2$。

由于 $\chi_D(47)=1$，$g_D$ 的普通单位根还是 $\alpha_{f,\sigma}$。普通模符号测度在恒等字符处给
$$L_{47}(g_D^\sigma,1)
=U_{f,\sigma}^2\,
\sigma\left(\frac{L(g_D,1)}{\Omega_{g_D}^+}\right)\ne0.
\tag{5.4}$$
非零性使用 R74 的严格中心值证书和 $U\ne0$，与周期的非零代数缩放无关。于是得到可直接用于实际计算的等价关系
$$\boxed{\quad
h_{\mathbb Q,\sigma}(y_f^{(D)},y_f^{(D)})\ne0
\quad\Longleftrightarrow\quad
L'_{47,\nu}(f^\sigma,1)\ne0.
\quad}\tag{5.5}$$
任何用非零 Shimura 周期得到的严格模符号导数非消失证书都能经 (5.5) 证明高度非消失。但若要把其**具体数值**代入 (4.1)，仍必须校准 (5.1) 和模符号周期，而不能仅由“同为 $L$ 函数”省去倍率。

## 6. 两个域的相容性与实际边界

每个轨道的有理 Mordell–Weil 模是秩一 $E_f$ 模。两组非挠 Heegner 向量因此满足
$$y_f^{(-163)}=b_f y_f^{(-43)},\qquad b_f\in E_f^\times.$$
故
$$\frac{C_{f,\sigma}^{(-163)}}{U_{f,\sigma}^4}
=\sigma(b_f)^2
\frac{C_{f,\sigma}^{(-43)}}{U_{f,\sigma}^4},\qquad
\frac{B_{f,\sigma}^{(-163)}}{E_{f,\sigma}^2}
=\sigma(b_f)^2
\frac{B_{f,\sigma}^{(-43)}}{E_{f,\sigma}^2}.
$$
因此 (4.2) 与用哪个 $K_D$ 提供秩一基无关。这是高度与对数双线性的结果，不是两个 $L$ 函数的数值相等。

本文消去了辅助素数 $47$ 的完全分裂假设障碍，并确定真正需要计算的圆分导数及其准确尺度。它本身没有求出这个导数，亦未计算 Chow–Heegner 平移 $\xi$、完整辅助局部高度或 R54 的共同根。即使实际导数都非零，全层 Serre 统一性仍要求随层识别联合有限靶的逆像。

## 7. 原始来源核对

- Daniel Disegni, **$p$-adic heights of Heegner points on Shimura curves**, *Algebra & Number Theory* **9** (2015), 1571–1646，DOI [10.2140/ant.2015.9.1571](https://doi.org/10.2140/ant.2015.9.1571)。[期刊全文](https://msp.org/ant/2015/9-7/ant-v9-n7-p03-s.pdf)：pp.1572–1575 的一般系数域、Heegner 点和 Theorems A、B；§4.4 的周期因子和 (4.4.1)；§5.1–5.2 的高度及基变换；Proposition 6.3.1(3) 的 Hodge 类 Hecke 作用。根会话逐项核对；上述式子是该定理在本题实际数据中的代入与后续推导。
- [同一论文 arXiv 版本](https://arxiv.org/pdf/1304.5204)：§4.4 明列周期相容性和字符因子；只作期刊文档的交叉核对。
- R68：实际极化、微分坐标与 BDP；R71：真实项链对应及 $47$ 处整右逆；R74：两个域的严格扭曲非消失和全部系数嵌入普通性。

本文没有把已发表 Gross–Zagier 定理记为新发现；新增的是本题实际层、实际同源与实际辅助素数的完整适用性及尺度核对。
