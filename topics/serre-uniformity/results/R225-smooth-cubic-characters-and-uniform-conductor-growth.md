# R225：三次光滑理想与一致有效的导子 $0.236933\ldots$ 次增长

日期：2026-11-13；会话：serre-uniformity-recovery。

**状态：已证明。** 本文加强 R116 的全素数、全 exceptional 有效结论。八个类数一底域 $K\ne\mathbb Q(\sqrt{-3})$ 上，实际小惯性三次角色的导子 $c$ 必须满足
$$
c\gg_\epsilon p^{\kappa_3-\epsilon},
\qquad
\kappa_3=\frac{e^{2/3}-1}{4}=0.2369335102\ldots.
$$
旧 R116 的指数为 $1/1000$。新证明保留变化模数 $c$ 的全部分班误差；坏素理想用正一填补，以精确光滑理想计数代替粗的有理素数计数。不要求 $j$ 整、分母非 exceptional 或中心值非零。

这是共同导子的必要下界，仍没有向上的统一控制。

## 1. 主定理

设 $E/\mathbb Q$、$p>37$ 属于本课题的实际完整非分裂正规化子设置，商域 $K$ 满足
$$
h_K=1,\qquad K\ne\mathbb Q(\sqrt{-3}),\qquad
\bar\rho_{E,p}(I_p)=C^3.
$$
令 $\eta$ 为 R66 的实际原始三次环类角色，其准确导子为 $c\mathcal O_K$。

**定理 225.1。** 对任意 $0<a<\kappa_3$，存在有效绝对常数 $P_a$，使所有上述实际曲线在 $p>P_a$ 时满足
$$
\boxed{c>p^a.}                                         \tag{225.1}
$$
这里 $P_a$ 同时适用于全部八个允许的类数一域，也不依赖于实际 $\eta$、新四阶惯性素数或潜在乘法素数。

等价地，对每个 $\epsilon>0$，存在有效正数 $C_\epsilon$，使对全部上述 $p>37$，
$$
\boxed{
c\ge C_\epsilon p^{\kappa_3-\epsilon},\qquad
h(\mathcal O_c)\ge C_\epsilon p^{\kappa_3-\epsilon},\qquad
D c^2\ge C_\epsilon p^{2\kappa_3-\epsilon},
}                                                        \tag{225.2}
$$
其中 $D=|D_K|$。三个不等式可以缩小至同一个有效 $C_\epsilon$。

## 2. 由实际曲线得到的同一个三次差角色

为每个允许的 $K$ 固定一条以 $\mathcal O_K$ 为复乘整环的有理曲线 $A_K$。固定有限集 $S_0$，包含 $2,3,D$ 及 $A_K$ 的坏约化素数。八个域有限，所有涉及这些选择的常数最终取有限最大值即可。$p\in S_0$ 的有限情形收入 $P_a$；以下 $p\notin S_0$。

R116 §§2–3 从 R21 的真实 Cartan 特征与 CM 特征比较得到一个复值原始三次 Hecke 角色 $\chi$，准确满足
$$
\mathfrak f(\chi)=cp\mathcal O_K,\qquad
\chi^3=1\ne\chi,\qquad
\chi^{\mathsf c}=\chi^{-1},\qquad p\nmid c.              \tag{225.3}
$$
这里 $\mathsf c$ 是复共轭，$\chi$ 是四次幂差角色，不是直接把 $\eta$ 改名。

更具体地，若 $\lambda$、$\psi$ 分别为实际 $E$ 与参考曲线的同向 Cartan 特征，$u=(p^2-1)/3$，$uv\equiv1\bmod3$，则
$$
\chi=(\lambda/\psi)^4=\eta^v\psi^{-uv}.
$$
$K$ 的单位阶为二或四，而 $4\mid u$，故 CM 主理想公式中的单位被杀掉。
令
$$
S=S_0\cup\{q:q\mid c\},\qquad
m=\operatorname{lcm}\left(c,\prod_{q\in S_0}q\right).
$$
有
$$
p\nmid m,\qquad m\le C_Kc.                              \tag{225.4}
$$
对 $S$ 外的主理想，准确主理想公式为
$$
\chi((z))=\rho_c(z\bmod c)\,\vartheta_p(z\bmod p),        \tag{225.5}
$$
其中 $\vartheta_p$ 是 $\mathbb F_{p^2}^{\times}$ 上非平凡三次乘法角色，$\rho_c$ 是模 $c$ 的有限角色。$p$ 在 $K$ 惰性，所以
$\mathcal O_K/p\simeq\mathbb F_{p^2}$。所有角色值和以后各分班权的绝对值至多一。

R116 引理 116.2 还给同一实际曲线的严格整数迹约束：
$$
\boxed{
q\notin S,\quad q<p,\quad q\text{ 在 }K\text{ 分裂},\quad
\chi(\mathfrak q)\ne1
\quad\Longrightarrow\quad p<256q^2.
}                                                        \tag{225.6}
$$
此处 $\mathfrak q\mid q$，并允许 $q$ 为 $E$ 的新四阶惯性素数。
该引理在实际全分歧循环好约化域上保留同一个整数迹 $b$，满足
$$
|b|<2\sqrt q,\qquad
b\equiv \zeta z+\zeta^{-1}\bar z\pmod{\mathfrak P},
\qquad \zeta^4=\chi(\mathfrak q)\ne1.
$$
当 $K\ne\mathbb Q(\sqrt{-3})$ 时，右侧特征零数不在 $\mathbb Q$；其与 $b$ 的非零范数被 $p$ 整除，而实域次数至多四，绝对值小于 $256q^2$。因此 (225.6) 依赖实际曲线，不能用任意抽象三次角色替代。

## 3. 对增长中模数 $c$ 一致的短箱求和

令 $\chi_0$ 为理想上的乘法函数：
$$
\chi_0(\mathfrak a)=
\begin{cases}
\chi(\mathfrak a),&(\mathfrak a,S)=1,\\
0,&(\mathfrak a,S)\ne1.
\end{cases}
$$
$\chi$ 本身在导子素理想处置零，特别 $\chi_0$ 在 $p$ 上方也为零。记
$$
\Sigma_0(T)=\sum_{N\mathfrak a\le T}\chi_0(\mathfrak a).
$$
对任意固定 $\nu>0$，置 $H=\lfloor p^{1/4+\nu}\rfloor$。
Chang [C09, Theorem 5] 给有效 $\delta_0=\delta_0(\nu)>0$，使充分大的 $p$ 上，对所有角色、$\omega\in\mathbb F_{p^2}\setminus\mathbb F_p$ 和任意平移的边长 $H$ 方框，一致有
$$
\left|\sum_{x\in I,\ y\in J}
\vartheta_p(x+\omega y)\right|
\ll_\nu p^{-\delta_0}H^2.                              \tag{225.7}
$$
取整可以先将 $\nu$ 换为稍小的正数并细分边界，得到此式。原文证明取
$\rho>1/4+2/k$ 后可用任意 $\delta<1/(4k^2)$，所以这里不是把未定量“充分大”擅自解释为有效。

**引理 225.2。** 对所有 $T\ge1$，
$$
\boxed{
|\Sigma_0(T)|\ll_{K,\nu}
Tp^{-\delta_0}+mH\sqrt T+m^2H^2.
}                                                        \tag{225.8}
$$
常数独立于 $c$、$p$、$\rho_c$ 和实际曲线。

**证明。** 写 $\mathcal O_K=\mathbb Z+\mathbb Z\omega$。
类数一使每个整理想恰有 $w_K$ 个生成元，故理想和是非零生成元和除以 $w_K$。
模 $m$ 的每个班可写成
$$
z=z_0+m(x+y\omega).
$$
式 (225.5) 中的模 $c$ 权以及与 $S$ 互素的指示权都在每班固定。模 $p$ 时 $m$ 可逆，所以可变部分是
$$
\vartheta_p(m)\,
\vartheta_p(x+y\omega+z_0/m).
$$
第二个角色的两个坐标只是区间的平移，(225.7) 对所有班一致。
在 $z\equiv0\bmod p$ 的点把 $\vartheta_p(0)$ 解释为零，准确保持原导子零值。

范数上界在每个 $(x,y)$ 平面给直径 $O_K(\sqrt T/m)$ 的同形椭圆。以边长 $H$ 的方框分割：全部 $m^2$ 个班内的完整方框的格点总数是 $O_K(T)$，所以其总和由 (225.7) 控为 $O_{K,\nu}(Tp^{-\delta_0})$，不能再乘一个 $m^2$。

每班遇到边界的方框所含格点至多
$$
O_K\!\left(H\frac{\sqrt T}{m}+H^2\right).
$$
乘全部 $m^2$ 个班，正是
$$
O_K(mH\sqrt T+m^2H^2).
$$
除去零元不增大误差。这证明 (225.8)，并显式保留 $c$ 随 $p$ 增长的全部代价。$\square$

## 4. 填补坏素理想后的消去界

令 $\mathcal T$ 包含 $S$ 上方的全部素理想及 $p\mathcal O_K$。定义完全乘法函数
$$
\widetilde\chi(\mathfrak p)=
\begin{cases}
1,&\mathfrak p\in\mathcal T,\\
\chi(\mathfrak p),&\mathfrak p\notin\mathcal T.
\end{cases}                                             \tag{225.9}
$$
现在每个整理想的值都属于 $\mu_3$。令 $g$ 为 $\mathcal T$-光滑理想的指示函数，即 $g(\mathfrak d)=1$ 当且仅当 $\mathfrak d$ 的素因子全部在 $\mathcal T$。因 $\chi_0$ 在这些素理想上均取零，有准确卷积式
$$
\widetilde\chi=\chi_0*g.                                 \tag{225.10}
$$

对任意固定 $\sigma>0$、$\epsilon_0>0$，存在有效常数满足
$$
\boxed{
\sum_{\mathfrak d}\frac{g(\mathfrak d)}{(N\mathfrak d)^\sigma}
=\prod_{\mathfrak p\in\mathcal T}
(1-(N\mathfrak p)^{-\sigma})^{-1}
\ll_{K,\sigma,\epsilon_0} c^{\epsilon_0}.
}                                                        \tag{225.11}
$$
证明中要把 $p$ 与 $c$ 分开：固定 $S_0$ 的贡献固定；$p$ 惰性，新增因子为
$(1-p^{-2\sigma})^{-1}\le(1-41^{-2\sigma})^{-1}$。其余素理想范数乘积至多 $c^2$。对足够大的范数 $n$ 用
$(1-n^{-\sigma})^{-1}\le n^{\epsilon_0/2}$，较小范数的有限乘积收入常数，即得 (225.11)。即使同一素数同时属于 $S_0$ 和 $c$，也只计一次或作安全的重复上界。

将 (225.8) 逐项代入 (225.10)。任取固定 $\tau>0$，并在三项中分别用 (225.11) 的 $\sigma=1,1/2,\tau$，得到
$$
\begin{aligned}
\left|\sum_{N\mathfrak a\le X}\widetilde\chi(\mathfrak a)\right|
&\ll
Xp^{-\delta_0}\sum_{N\mathfrak d\le X}\frac{g(\mathfrak d)}{N\mathfrak d}
+mH\sqrt X\sum_{N\mathfrak d\le X}
\frac{g(\mathfrak d)}{\sqrt{N\mathfrak d}}
+m^2H^2\sum_{N\mathfrak d\le X}g(\mathfrak d)\\
&\ll_{K,\nu,\tau,\epsilon_0}
c^{\epsilon_0}\left(
Xp^{-\delta_0}+mH\sqrt X+m^2H^2X^\tau\right).
\end{aligned}                                           \tag{225.12}
$$
末项使用
$\sum_{N\mathfrak d\le X}g(\mathfrak d)
\le X^\tau\sum g(\mathfrak d)/(N\mathfrak d)^\tau$。
这是处理所有短自变量 $X/N\mathfrak d$ 的准确方式；没有把只在大自变量有效的消去式硬套到长除数。

## 5. 实际迹迫使光滑理想具有正质量

置
$$
Y=\frac{\sqrt p}{17}.
$$
对每个 $N\mathfrak q\le Y$ 的素理想，
$$
\boxed{\widetilde\chi(\mathfrak q)=1.}                  \tag{225.13}
$$
在 $\mathcal T$ 内由定义成立。其余素理想不在 $K$ 的分歧素数上方。
若对应惰性有理素数，复共轭固定该素理想，而 $\chi^{\mathsf c}=\chi^{-1}$，故它的值既平方为一又立方为一，只能为一。若对应分裂素数 $q$，则其范数为 $q$，$q<p$，且 (225.6) 排除非一值，因为
$$
256q^2\le\frac{256}{289}p<p.
$$
这逐项证明了 (225.13)。

固定任意
$$
1<u<e^{2/3}<2.
$$
R224 §4 的完整光滑理想计数给，对 $y=X^{1/u}$，
$$
\Psi_K(X,y)=\kappa_KX(1-\log u)+O_{K,u}(X/\log X),
\qquad A_K(X)=\kappa_KX+O_K(\sqrt X).                    \tag{225.14}
$$
此处只用固定域的格点计数、$y^2>X$ 的唯一大素因子公式和 Garcia–Lee 的无条件有效 Mertens 定理。

若 $y\le Y$，则所有 $y$-光滑理想的 $\widetilde\chi$ 值为一，而其他三次单位根的实部为 $-1/2$。因此
$$
\begin{aligned}
\operatorname{Re}\sum_{N\mathfrak a\le X}\widetilde\chi(\mathfrak a)
&\ge\frac32\Psi_K(X,y)-\frac12A_K(X)\\
&=\kappa_KX\left(1-\frac32\log u\right)
+O_{K,u}(X/\log X).
\end{aligned}                                           \tag{225.15}
$$
因 $u<e^{2/3}$，主项系数严格为正，且全部常数有效。

## 6. 参数同时选择，得到精确临界指数

固定 $0<a<\kappa_3$，反设 $c\le p^a$。由
$$
\frac12+2a<\frac{e^{2/3}}2,
$$
可有效选取固定实数 $s,u$ 满足
$$
\frac12+2a<s<\frac{e^{2/3}}2,\qquad
2s<u<e^{2/3}.
$$
置 $X=p^s$。由于 $s/u<1/2$，
$$
X^{1/u}\le\frac{\sqrt p}{17}
$$
对充分大的 $p$ 有效成立。于是 (225.15) 给
$$
\operatorname{Re}\sum_{N\mathfrak a\le X}\widetilde\chi(\mathfrak a)
\ge c_{K,u}X>0                                          \tag{225.16}
$$
其中 $c_{K,u}$ 是有效的固定正数。

再有效选择 $\nu>0$，使
$$
\beta:=\frac s2-a-\frac14-\nu>0.
$$
由 $m\le C_Kc$，
$$
\frac{mH}{\sqrt X}\ll_K p^{-\beta}.                     \tag{225.17}
$$
Chang 的 $\delta_0(\nu)>0$ 已固定。取
$$
\tau=\frac{\beta}{2s}>0,\qquad
0<\epsilon_0<
\frac{\min(\delta_0,\beta)}{2(a+1)}.
$$
将 (225.12) 除以 $X$，用 $c\le p^a$ 和 (225.17)，得到一致有效的
$$
\begin{aligned}
\frac1X\left|\sum_{N\mathfrak a\le X}\widetilde\chi(\mathfrak a)\right|
&\ll_{K,a}
p^{a\epsilon_0-\delta_0}
+p^{a\epsilon_0-\beta}
+p^{a\epsilon_0-2\beta+s\tau}\\
&=
O_{K,a}\left(
p^{a\epsilon_0-\delta_0}
+p^{a\epsilon_0-\beta}
+p^{a\epsilon_0-3\beta/2}\right)
\longrightarrow0.
\end{aligned}                                           \tag{225.18}
$$
三个指数均严格为负。这里 $\epsilon_0$ 在已选定的 Chang 消去幂之后选择；没有用一个固定的 $c$ 依赖常数去控制变化中的 $c$。

式 (225.18) 与 (225.16) 矛盾。所有阈值均可有效求出，最后在八个 $K$ 上取有限最大值，即证 (225.1)。

临界值来自两项独立限制：
$$
X>c^2p^{1/2+o(1)},\qquad
\frac{\log X}{\log(\sqrt p)}<e^{2/3}.
$$
合并恰为
$$
a<\frac{e^{2/3}-1}{4}.
$$
本文不主张达到没有 $\epsilon$ 损失的端点。

## 7. 全部素数、类数和共同导子

给定 $0<\epsilon<\kappa_3$，在定理 225.1 中取比
$\kappa_3-\epsilon$ 稍大的 $a$。有限范围 $37<p\le P_a$ 只需用 $c\ge1$，通过有效缩小常数即可得到 (225.2) 的第一个不等式。若 $\epsilon\ge\kappa_3$，较小 $\epsilon$ 的结果已经蕴含所需弱化。

环类数公式给
$$
h(\mathcal O_c)
=\frac{c}{[\mathcal O_K^\times:\mathcal O_c^\times]}
\prod_{q\mid c}\left(1-\frac{\chi_K(q)}q\right)
\ge\frac{\varphi(c)}3.
$$
对每个 $\xi>0$，初等有效估计为
$$
\varphi(c)\gg_\xi c^{1-\xi}.
$$
可逐个大素因子用 $(1-1/q)\ge q^{-\xi}$，有限小素因子收入常数。先在 $c$ 的界中取稍小的指数损失，再选 $\xi$，即得
$h(\mathcal O_c)\gg_\epsilon p^{\kappa_3-\epsilon}$，无需 Siegel。

最后 $D\ge3$，故第一个界平方给
$Dc^2\gg_\epsilon p^{2\kappa_3-\epsilon}$。R214 的共同导子
$M^*=D(bc)^2$ 亦至少为此量；这里没有控制可能任意增长的新四阶因子 $b$。

## 8. 范围与来源

本证明的参数 $c$ 可以随 $p$ 增长至临界幂以下，$\rho_c$ 和新四阶支撑全部可变。它对 nonexceptional、exceptional、整 $j$ 和非整 $j$ 分支同时成立。三次角色在 $p$ 的非平凡性与实际迹障碍都保留；前者给短箱消去，后者给小素理想上的恒一窗口。

$K=\mathbb Q(\sqrt{-3})$ 不满足 (225.6) 的非零范数前提，不能混入有限最大值。该域 $c=6,9$ 的实际整 $j$ 四次支撑增长由 R224 另行处理，但其导子上界及其他变化 $c$ 分支仍未解决。

参考：

- [R116](R116-fixed-class-one-cubic-conductor-prime-bound.md) §§2–3：实际差角色、准确 $cp$ 导子、主理想公式及 $p<256q^2$ 的同一真实迹约束；§7 给原 $1/1000$ 指数。
- [R224](R224-smooth-ideal-detection-and-integral-j-conductor-growth.md) §4：固定虚二次域的有效光滑理想计数，特别 $1<u<2$ 的精确主项。
- M.-C. Chang，*Burgess Inequality in $\mathbb F_{p^2}$*，Geometric and Functional Analysis **19** (2009), 1001–1016，**Theorem 5**；证明见刊页1007–1008，式 (4.2) 及末行给参数和有效消去幂。[期刊全文](https://link.springer.com/content/pdf/10.1007/s00039-009-0031-5.pdf)，[作者机构存档](https://escholarship.org/content/qt4xv8h0mj/qt4xv8h0mj.pdf)。
- S. R. Garcia、E. S. Lee，*Unconditional explicit Mertens' theorems for number fields and Dedekind zeta residue bounds*，The Ramanujan Journal **57** (2022), 1169–1191，**Theorem 1, (B1)–(B2)**。[DOI](https://doi.org/10.1007/s11139-021-00435-6)，[对应作者稿](https://arxiv.org/html/2007.10313v4)。

