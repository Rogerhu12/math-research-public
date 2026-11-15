# R828 — 原惰性 CM 源的二部分交换、new 两列零值与 old 子空间

**状态：已证明。** 对原允许 $p\ge41,\ p\equiv11\pmod {12}$，GC/IH 的两个指定原源值 $e_{G_1,p},e_{G_5,p}$ 均为零；由 R826，它们的两个指定 Gaussian companion theta CM 值也为零。证明使用一个真正与有限 Weil/CM 作用交换的等距，不从两个投影为零直接反推源值为零。

本篇还完全分类保持原 EO 子空间的二次模等距：在剩余六维 old 子空间上，这类等距只给标量。因此本篇不产生六项原 FG 组合的非零，也不处理 primitive/Legendre 筛。

来源：
- [GC 原固定射线类分解](../notes/2026-11-15-sigma-inert-Gaussian-rayclass-source.md)；
- [R826 原 companion CM 配对](R826-original-inert-companion-theta-CM-pairing.md)；
- [R826 实际固定运输](R826-certified-inert-Gaussian-source-transport.md)；
- [R812 原 theta/Miller 标架](R812-original-apolar-source-and-Gaussian-Frobenius-low-moment.md)。

## 1. 原二次模与交换算子

令
$$
 \mathcal A=(\mathbb Z/6\mathbb Z)^2,\qquad
 q(r,s)=\frac{r^2+s^2}{12}\pmod{\mathbb Z},
$$
$$
 b((r,s),(r',s'))=\frac{rr'+ss'}6\pmod{\mathbb Z}.
 \tag{828.1}
$$
这就是两份原 level-six theta 特征的二次模。定义
$$
 P_2=\begin{pmatrix}4&3\\3&4\end{pmatrix}\pmod6,\qquad
 (\mathscr P M)(r,s)=M(P_2(r,s)).
 \tag{828.2}
$$
它在模 $2$ 部分交换两个坐标，在模 $3$ 部分保持各坐标不变。直接计算
$$
 P_2^2=\begin{pmatrix}25&24\\24&25\end{pmatrix}\equiv I\pmod6,
$$
$$
 q(P_2(r,s))-q(r,s)=2(r+s)^2\in\mathbb Z.
 \tag{828.3}
$$
故 $\mathscr P^2=1$，且 $P_2$ 是二次模等距。

原单份 theta 的 Weil $T$ 矩阵为 $e(r^2/12)$ 对角阵；$S$ 矩阵在一个共同的非零标量之外，其核为 $e(-rr'/6)$。两份张量的相位和核就是 (828.1)。由 (828.3)，$\mathscr P$ 与 $T$ 交换；由 $P_2^tP_2\equiv I\pmod6$，变换求和指标可见它与 $S$ 的 Fourier 核交换。共同的 metaplectic 或 eta 标量不改变交换关系。因此
$$
 \mathscr P\,\rho_{\mathcal A}(\gamma)
  =\rho_{\mathcal A}(\gamma)\,\mathscr P
 \quad(\gamma\in\mathrm{SL}_2(\mathbb Z)).
 \tag{828.4}
$$
这不是在有限稀疏单项式上任意施加对角权。

设 $\iota_1(r,s)=(-r,s)$、$\iota_2(r,s)=(r,-s)$。矩阵 (828.2) 与两者模 $6$ 交换，因为相关非对角项只相差 $6$。所以 $\mathscr P$ 保持原
$$
 V_{\rm EO}
 =\{M:\ M(-r,s)=M(r,s),\ M(r,-s)=-M(r,s)\}.
 \tag{828.5}
$$
这个空间维数为 $4\cdot2=8$。

所有上述恒等式先在含有限 theta 相位的数域上成立；对 $p>3$ 约化时同样成立。涉及的 Fourier 分母只有 $2,3$。

## 2. 原六个 old 列与两个 new 列正是正负空间

仍取 GC 原次序
$$
 F_3(t),F_3(t^2),F_3(t^4),
 F_7(t),F_7(t^2),F_7(t^4),G_1(t),G_5(t)
 \tag{828.6}
$$
及其八个原 harmonic 系数矩阵 $M_\nu$。GC 的整基证明给出它们在 $V_{\rm EO}$ 中线性无关，且除 $2$ 外没有基变换分母。

这里可直接从 GC 系数公式核 $\mathscr P$ 的符号。记 $c=r+is\bmod6$；$P_2$ 保持 $c\bmod3$，只交换 $r,s$ 的奇偶。

- $F_b$ 的三种 old 系数只依赖 $c\bmod3$ 以及三种对称奇偶类型：一奇一偶、两奇、两偶。涉及 $c/(1+i)$ 或 $c/2\bmod3$ 的字符也只依赖 $c\bmod3$。故它们在 $P_2$ 下不变。
- $G_b$ 的系数只支撑在一奇一偶类型；该处的模 $2$ 字符 $\delta(c)$ 在两种奇偶顺序之间变号，而模 $3$ 字符不变。故它们在 $P_2$ 下变号。
- GC 的 harmonic 投影是 $(C(r,s)-C(r,-s))/(2i)$。由 $\mathscr P$ 与 $\iota_2$ 交换，上述符号保留到原 $M_\nu$。

于是
$$
 \mathscr P M_{F_b,d}=M_{F_b,d},\qquad
 \mathscr P M_{G_b}=-M_{G_b}.
 \tag{828.7}
$$
因为 $p\ne2$ 且八矩阵是整基，
$$
 V_{\rm EO}=V_+\oplus V_-,
$$
$$
 V_+=\langle M_{F_3,1},M_{F_3,2},M_{F_3,4},
                 M_{F_7,1},M_{F_7,2},M_{F_7,4}\rangle,\qquad
 V_-=\langle M_{G_1},M_{G_5}\rangle.
 \tag{828.8}
$$
维数分别为 $6,2$。

## 3. 原 $U$、共同相位与 CM 允许子空间

使用 R812 原 Miller/Heisenberg 矩阵
$$
 U(P_0)=c\,\widehat U
$$
及原行次序 $(S,F,H,R,J,G)$。定义
$$
 \mathcal U(M)=\widehat U M\widehat U^t.
 \tag{828.9}
$$
由 R812 的奇偶核对，(828.9) 将 $V_{\rm EO}$ 同构送到原 $(S,F,H,R)\times(J,G)$ 的八维矩阵空间。$c$ 是所有行的共同尺度；它既不改变子空间，也不改变 (828.9) 的共轭关系。R812 认证的分母与 determinant Norm 保证 $\widehat U$ 及其逆在每个 $p\ge41$ 的允许嵌入下均整且可逆。

取原 $\zeta^3=1,\ \zeta\ne1$。由 $\sigma(\zeta z)=\zeta\sigma(z)$、$x(\zeta z)=\zeta x(z)$、$y(\zeta z)=y(z)$，原六截面的实际 CM 字符矩阵为
$$
 C_\zeta=\operatorname{diag}(1,\zeta,\zeta^2,1,1,\zeta).
 \tag{828.10}
$$
因此原 EO 八行
$$
 (S,J),(S,G),(F,J),(F,G),(H,J),(H,G),(R,J),(R,G)
$$
的字符依次为
$$
 1,\zeta,\zeta,\zeta^2,\zeta^2,1,1,\zeta.
 \tag{828.11}
$$
原 critical 总次数为 $p-6\equiv2\pmod3$，所以 CM 允许空间正是
$$
 W_{\rm orig}=\langle E_{F,G},E_{H,J}\rangle.
 \tag{828.12}
$$

必须核定 $\mathscr P$ 保持其原像，不能只在 (828.12) 上写一个期望的投影。R812 的实际 theta 基在 CM 稳定元下按原有限 Weil 矩阵变换；eta 与半权规范仅带来一个共同标量。若按列约定将该实际矩阵记作 $\rho_{\rm CM}$、共同标量记作 $a_{\rm CM}$，则原基恒等准确写成
$$
 C_\zeta U=a_{\rm CM}U\rho_{\rm CM}.
 \tag{828.13}
$$
这里不将 $a_{\rm CM}$ 置为 $1$。若用逆的模变换约定，$\rho_{\rm CM}$ 与相位同时替换为对应逆；(828.4) 对这两种约定都成立。

在两份张量上，(828.13) 给出
$$
 \mathcal U(\rho_{\rm CM}M\rho_{\rm CM}^t)
  =a_{\rm CM}^{-2}\,
       C_\zeta\mathcal U(M)C_\zeta^t.
 \tag{828.14}
$$
故
$$
 W=\mathcal U^{-1}(W_{\rm orig})
 \tag{828.15}
$$
是源 CM 作用的一个特征空间，特征值为共同相位乘 $\zeta^2$。由 (828.4)，$\mathscr P$ 与这个实际 CM 作用交换，于是 $W$ 在 $\mathscr P$ 下稳定。共同相位和 $c$ 均已保留；证明不依赖随意改变原 theta 相位。

## 4. 实际零列与严格的交零论证

实际公开运输已认证
$$
 \mathcal U(M_{G_1})_{FG}
 =\mathcal U(M_{G_1})_{HJ}
 =\mathcal U(M_{G_5})_{FG}
 =\mathcal U(M_{G_5})_{HJ}=0.
 \tag{828.16}
$$
这是数域中的精确零，二十四个有理幂基坐标均为零。

来源为公开 run 43725592504、job 132846716428、source commit d3a4216875ffde37005c74a8cf27687e631d935a；实际 core SHA256 为 70e565af2b00f2ad7a58f555bffd177f7a277d8a8c01dd49b6f6dde26d25de38，canonical JSON SHA256 为 916e1b951a5acc6c375477ea13078d27a088ffcebac66ab76abf7a91676836a3。该计算同时输出完整原 $\widehat U$、source 基矩阵和八维运输矩阵；本篇只读取已有结果，不重跑任何运算。重算所需源码、参数和运行记录见前引实际结果文件。

由 (828.8)、(828.12)、(828.16)，
$$
 V_-\cap W=0.
 \tag{828.17}
$$
证明如下：若 $v\in V_-\cap W$，则 $\mathcal U(v)$ 只能支撑在 FG/HJ 两行；另一方面 (828.16) 又使这两行都为零。因此 $\mathcal U(v)=0$，由原 $\mathcal U$ 可逆得 $v=0$。

由于 $W$ 在 $\mathscr P$ 下稳定，对 $w\in W$，
$$
 w_-=\frac{w-\mathscr Pw}{2}\in W\cap V_-=0.
$$
因此
$$
 \boxed{\ W\subset V_+.\ }
 \tag{828.18}
$$
这一步使用了真正的交换关系和交零论证。单独的 (828.16) 并不足以推出 (828.18)。

## 5. 原两个 CM 源值准确为零

GC 的原源矩阵是
$$
 M(p)=\sum_\nu e_{\nu,p}M_\nu.
 \tag{828.19}
$$
IH/R826 已在原标架证明
$$
 (Q-Q_{\rm poly})(P_0)=\frac{c^2}{32}\mathcal U(M(p)),
 \qquad Q_{\rm poly}(P_0)=0.
 \tag{828.20}
$$
原 CM 权 (828.11) 使 (828.20) 右侧只可能有 FG/HJ 两行。因此 $M(p)\in W$。由 (828.18) 和整基分解 (828.8)，
$$
 \boxed{\ e_{G_1,p}=e_{G_5,p}=0.\ }
 \tag{828.21}
$$

R826 的逐项五次 companion 公式为
$$
 e_{\nu,p}
 =-\frac{120\,12^5}{d_0}B^5\,
      \mathscr C_{\nu,p}(P_0).
 \tag{828.22}
$$
外因子对 $p\ge41$ 为单位，故也有
$$
 \boxed{\ 
 \mathscr C_{G_1,p}(P_0)
 =\mathscr C_{G_5,p}(P_0)=0.
 \ }
 \tag{828.23}
$$
这些 companion theta 本身的全局首项不为零；(828.23) 是固定原 CM 点值的消失。这给出本链中一个具体例子：全局 theta 非零不能替代指定 CM 值非零。

原 FG 组合因而只剩六个 old 值：
$$
 \sum_{j=0}^{N-1}(-1)^j f_{N-1-j}g_j
 =-\frac{120c^2}{d_0}
   \sum_{\substack{b=3,7\\d=1,2,4}}
      \kappa_{b,d}\,\mathscr C_{b,d,p}(P_0).
 \tag{828.24}
$$
(828.21) 不等同于三种 old level 点值相等；它没有删掉任何 $d^{p-7}$、CM 标记或原共同尺度。

## 6. 保持原 EO 的全部二次模等距

这一小分类明确说明，在同一等距来源中还有没有另一个未使用的投影。

主分解 $\mathcal A=\mathcal A_2\oplus\mathcal A_3$ 下，用 $r=3r_2+4r_3$ 表示单坐标，可得
$$
 q_2(r_2,s_2)=\frac34(r_2^2+s_2^2),\qquad
 q_3(r_3,s_3)=\frac13(r_3^2+s_3^2).
 \tag{828.25}
$$
任何群自同构必须保持主分解。

在 $\mathcal A_2$ 中，三个非零向量的二次值分别为 $3/4,3/4,1/2$。故等距必须固定 $(1,1)$，而可以交换两坐标；只有恒等与交换两个等距。

在 $\mathcal A_3$ 中，$r^2+s^2$ 是各向异性二次型。范数 $1$ 的向量恰为
$$
 (\pm1,0),(0,\pm1).
$$
一旦选定标准第一基向量的像，与之正交且范数 $1$ 的第二基向量只有两个选择。因此全部八个等距正是有符号置换矩阵。

所以全二次模等距群有 $2\cdot8=16$ 个元素。模 $3$ 部分不交换坐标时，它由两坐标反号及 $P_2$ 生成；这些元素保持 $V_{\rm EO}$。模 $3$ 部分交换坐标时，它把两个反号算子互换，因而把 $V_{\rm EO}$ 送到 $V_{\rm OE}$。在特征不为 $2$ 时，后者与 $V_{\rm EO}$ 交为零，故这类元素不保持原 EO 空间。

于是保持原 EO 的等距全部由
$$
 \iota_1,\quad\iota_2,\quad P_2
 \tag{828.26}
$$
生成。在 $V_{\rm EO}$ 上，前两者分别为标量 $+1,-1$；在剩余的 $V_+$ 上，$P_2$ 也为 $+1$。因此：

> 由这个原二次模等距群、并保持原 EO 通道所得的全部作用，在剩余六维 old 子空间上都是标量。

若把不保持 EO 的等距先作用、再投回 EO，所得为零；所以其线性组合也不能在 $V_+$ 上产生额外的非标量投影。这里没有声称整个 Weil 表示的所有抽象交换子都已分类；结论只针对上述真实二次模等距及其通道保持作用。

## 7. 剩余问题

(828.24) 六个系数虽已由实际固定运输认证为允许 $p$ 下的单位，但六个原 CM 值仍可能发生消失或相消。不能把 U₂ 关系中不同的 $q,-q,q^2,q^4$ 标记无证合并，也不能由剩余二维允许空间的维数推出指定 FG 坐标非零。

下一步需要新的、保留原 level 与尺度的 CM 配对或算术输入；本篇的全部等距作用已用尽其在原 EO old 空间上的非标量部分。原同一 primitive $h$ 与 Legendre 因子的共同非零仍未解决。
