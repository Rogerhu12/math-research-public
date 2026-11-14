# R80：完整 Cartier 后仍保留移动 Hasse 留数

日期：2026-11-12。状态：实际双留数、统一零点界和支撑下界已证明。
完整证明及原始来源见[完整 Cartier 与移动 Hasse 留数](../notes/2026-11-12-full-cartier-and-moving-hasse-residues.md)。

本结论只检验当前实际带权 Kummer 输入能否直接降到固定极点空间，
不排除其他有限几何比较，也没有证明或否定本课题的无穷素数目标。

## 1. 固定单位与真实 GM 权重必须分别保留

固定代数单位的整 Kummer cochain 模 $p$ 可写成
$P_p/D^p$，其中 $D$ 固定、$\deg P_p=O(p)$。
完整 Cartier 将其有理顶次形式的极点阶除以 $p$，因而单独这一输入确有固定次数控制。

但 R78 的实际临界导数行使用

$$
\Omega_p=\zeta_p^2\,dh_e\wedge d\log Z,
\qquad \zeta_p=U/V,\quad Z=-x/y.
$$

R79 的全形式盘结论可推广到实际全基晶体：
$\bar U,\bar V\in\mathbb F_p[t,s^{-1}]$、$V=H/(h s^p)$。
准确 Wronskian 给 $U(\alpha)V'(\alpha)=s(\alpha)^{-p-1}\ne0$。
因此 $\zeta_p$ 在每个 Hasse 根 $\alpha$ 处都有真简单极点，
写为 $A_\alpha/(t-\alpha)+B_\alpha+\cdots$。

## 2. 原轨道中两个截面的真实双留数

取实际标签 $P=(1,-1)/68$、$Q=-3P$，令 $z_P=Z(-P_t)$、$z_Q=Z(-Q_t)$。
二者阶均为 $68$，所以在所有光滑纤维上为非零有限值，且 $Z$ 在该点为 étale 坐标。
实际单位的共同除子贡献不能丢；两截面处的准确对数留数均为

$$
m_P=m_Q=\frac{c_e(273+16i)}{578},
$$

它在每个惰性 $p\ge7$ 为单位。
先沿基点、再沿纤维截面取对数留数，得到

$$
\operatorname{Res}_{(\alpha,-P)}\Omega_p
=-m_PA_\alpha^2
\left((\log z_P)''+2\frac{B_\alpha}{A_\alpha}(\log z_P)'\right).
$$

其中纤维二阶极点与 $1/Z$ 的乘积产生必要的简单留数。
完整 Cartier 将该非零双留数取 $p$ 次方根，故保留真对数极点。

## 3. 固定 Wronskian 给线性支撑下界

令 $f_P=(\log z_P)'$、$f_Q=(\log z_Q)'$、
$\Delta=f_P'f_Q-f_Q'f_P$。
若 $\Delta\ne0$，上述两个双留数不可能同时为零。
在实际 $\lambda=1$ 的指定 cusp，$w=q^{1/68}$，直接 Tate 展开给

$$
\Delta=\frac{12\varepsilon^2}{(-544)^3}w^{-100}+O(w^{-98}),
\qquad \varepsilon=\zeta_{68}.
$$

故它在每个目标特征都非零。取实际 Legendre 全级点 torsor 的一个连通分量，
正规紧化到 $C$，记到 $\lambda$ 线的次数为 $d$。
不将其未经论证认定为 coarse 模曲线 $X(68)$。
SGA 1 的 tame specialization 与相对 Abhyankar 保持其良好约化、连通性及 cusp 惯性；
适用是因为实际群阶仅含 $2,3,17$。

每个有限 cusp 的 $\Delta$ 极阶至多 $3e$，无穷远无极点。
因此全部零点数含重数至多 $6d$，至多六个 Hasse 底点能使所有全级点均例外。
准确得到

$$
\boxed{\quad
\mathscr C_2(\Omega_p)\text{ 至少在 }
\frac{p-1}{2}-6\text{ 个不同 Hasse 底点上有真对数极点。}
\quad}
$$

对惰性 $p\ge19$ 下界为正。非零双留数也不能通过加有理恰当二形式消去。

**剩余任务：** 若继续有限维化，须证明实际配对、完整 isogeny trace 或更大系数系统
对这些移动留数的额外作用；极点阶下降本身不提供固定支撑，更不直接计算最终中央标量。
