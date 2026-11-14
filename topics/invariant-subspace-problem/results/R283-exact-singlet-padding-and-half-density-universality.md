# R283：惰性配对填充把全部有限 primitive 问题精确嵌入半密度上侧

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：已证明。** 对任意有限正权 Boolean 行，可添加实际正权位，使全部旧真实 primitive Gram 成为新模型的共同正交约化块，同时使最大单平方权占比 $\delta$ 任意小，并使物理出生密度 $s\delta$ 落在 $1/2$ 上方的任意窄带。这是精确有限维嵌入，不是无穷权近似。它没有证明一般相邻正性；它说明仅靠稀释 $\delta$ 而不支付新增出生，不能把一般问题放入既有低占据范围。

## 1. 一个实际两位惰性因子

两个同正权 $a$ 的物理位上，取单位向量
$$
\psi=\frac{e_{\{1\}}-e_{\{2\}}}{\sqrt2}.
$$
令 $D_{\rm pair}=a(E_1+E_2)$。逐基作用立刻给
$$
D_{\rm pair}\psi=0,\qquad D_{\rm pair}^*\psi=0.
\tag{1.1}
$$
因此 $\mathbb C\psi$ 是删除及伴随的共同正交约化直线，物理出生为一，串长为零。它不是一个从模型中删除的形式位。

对 $2k$ 个同权 $a$ 的位按两位分组，置
$$
\Psi_k=\psi^{\otimes k}.
$$
其范数为一，精确物理次数为 $k$，且整个池删除 $D_{\rm pool}$ 及其伴随均在该线上为零。$k=0$ 时取真空标量。

## 2. 全部完整逆与 primitive Gram 的精确共同约化

取任意旧 $N$ 位正权行 $D$，令
$$
\widetilde D=D\otimes I+I\otimes D_{\rm pool}
$$
为加入上述 $2k$ 位后的实际 Boolean 算子。定义等距映射
$$
U_kx=x\otimes\Psi_k.
$$
由 (1.1)，
$$
\widetilde D U_k=U_kD,\qquad
\widetilde D^*U_k=U_kD^*.
\tag{2.1}
$$
因此 $\operatorname{Ran}U_k$ 同时正交约化两算子，并把旧物理层 $\mathcal H_p$ 等距送到新层 $\widetilde{\mathcal H}_{p+k}$。

固定旧出生 $s$，记 $K_s=\ker D\cap\mathcal H_s$。新出生为 $\widetilde s=s+k$，新位数为 $\widetilde N=N+2k$，所以最高合法高度**恰好不变**：
$$
\widetilde N-2\widetilde s=N-2s.
\tag{2.2}
$$
对任意合法 $0\le j\le N-2s$，完整层 Gram 为
$$
F_{j,s}=\frac{D^j(D^*)^j}{(j!)^2}\bigg|_{\mathcal H_s},\qquad
\widetilde F_{j,s+k}=\frac{\widetilde D^j(\widetilde D^*)^j}{(j!)^2}
\bigg|_{\widetilde{\mathcal H}_{s+k}}.
$$
二者都是合法完整层上的正可逆算子。(2.1) 给
$$
\widetilde F_{j,s+k}U_k=U_kF_{j,s},\qquad
\widetilde F_{j,s+k}^{-1}U_k=U_kF_{j,s}^{-1}.
\tag{2.3}
$$
没有先压缩 Gram 再求逆：第二式来自真正正交约化块的完整逆。

同样，$U_kK_s$ 是新 primitive 空间的正交约化分支；其正交投影满足
$P_{\widetilde K_{s+k}}U_k=U_kP_{K_s}$。因此实际 primitive Gram
$$
\Gamma_{j,s}=P_{K_s}F_{j,s}^{-1}|_{K_s}
$$
满足完整共同身份
$$
\boxed{\widetilde\Gamma_{j,s+k}U_k=U_k\Gamma_{j,s}
\quad\text{在 }K_s\text{ 上，全部合法 }j.}
\tag{2.4}
$$
特别，任一相邻缺陷
$$
C\Gamma_{n-1,s}-\Gamma_{n,s}\Gamma_{n+1,s}^{-1}\Gamma_{n,s}
$$
原样成为新缺陷的共同正交约化块。旧严格违反、零缺陷方向和全部该分支的最佳相邻比都准确保留。没有使用维数极限、条件数运输或弱收敛。

## 3. 任意窄半密度上侧带中的精确副本

记旧总平方权与最大平方权为
$$
S=\sum_{i=1}^N b_i^2,\qquad M=\max_i b_i^2.
$$
先设 $s\ge1$。选择有限正权 $a$ 使
$$
a^2>\max\{M,S/(2s)\},\qquad q=S/a^2\in(0,2s).
\tag{3.1}
$$
在 §2 的新模型中，最大平方权为 $a^2$，总平方权为 $S+2ka^2$。所以
$$
\widetilde\delta=\frac1{q+2k},\qquad
\boxed{(s+k)\widetilde\delta
=\frac12+\frac{2s-q}{2(q+2k)}.}
\tag{3.2}
$$
对每个有限 $k$，右侧严格大于 $1/2$；当 $k\to\infty$，它从上方趋于 $1/2$，同时 $\widetilde\delta\to0$。

给定任意 $\varepsilon>0$、$\delta_0>0$，只需取整数 $k\ge1$ 满足
$$
k>\max\left\{
\frac{\delta_0^{-1}-q}{2},\quad
\frac{2s-q}{4\varepsilon}-\frac q2
\right\},
\tag{3.3}
$$
便准确有
$$
\boxed{0<\widetilde\delta<\delta_0,\qquad
\frac12<\widetilde s\widetilde\delta<\frac12+\varepsilon.}
\tag{3.4}
$$
所有新增权和位数均有限，且原全部合法高度保持。

旧出生 $s=0$ 时，先添一个任意同权配对因子。由 §2，旧模型原样进入新出生一的约化分支；随后对这个有限模型使用 (3.1)–(3.4)。因此结论覆盖旧出生零，而非默默排除真空问题。

## 4. 任意薄带已包含最优普适常数问题

固定任意合法相邻高度 $n\ge1$，令 $\mathcal C_n$ 表示对全部有限正权、全部合法出生求上确界的最佳实际相邻比。对给定 $\varepsilon,\delta_0>0$，只把模型限制在
$$
0<\delta<\delta_0,\qquad \frac12<s\delta<\frac12+\varepsilon
\tag{4.1}
$$
中求同一上确界，记为 $\mathcal C_n(\varepsilon,\delta_0)$。由 (2.4) 和 §3，任一旧模型的比都是某个 (4.1) 模型内共同约化分支的准确比，故
$$
\mathcal C_n\le\mathcal C_n(\varepsilon,\delta_0).
$$
反向是取上确界的集合包含关系。因此包括可能的无穷值在内，
$$
\boxed{\mathcal C_n=\mathcal C_n(\varepsilon,\delta_0)
\quad\text{对每个 }n\ge1,\ \varepsilon,\delta_0>0.}
\tag{4.2}
$$
所以在任意这样薄的半密度上侧带上证明一个权和位数无关的首边常数 $C$，已经等价于证明全部有限模型的首边同一常数。再由 [R281 的极强位传输](R281-heavy-bit-height-transfer-and-sharp-universal-first-edge-lower-bound.md)，这也等价于整个有限 primitive 全高度同一常数问题。

R281 的等权中央边回传已经证明普适首边常数至少为一。因此即使加上任意小的 $\delta$ 和任意薄的 (4.1) 限制，其最优普适首边常数仍至少为一；没有用数值猜测得出此下界。

## 5. 与低占据定理的严格边界

[玻色仿射传输](R279-bosonic-affine-primitive-gram-transfer-and-low-occupation-bounds.md) 已付的首边范围是 $s\delta\le1/(2\sqrt2)$。本稿精确副本落在 $s\delta>1/2$，并没有进入那个范围。

因此，减少单个位的相对权而忽略物理出生的增长，会造成错误推论。相反，如果未来能把一个普适首边常数扩展到整个 $s\delta<1/2+\varepsilon$ 的范围，哪怕只有任意一个固定 $\varepsilon>0$，本稿就足以把它转成全部有限模型的同一常数。该条件范围本身已经包含完整难题，不是一个可以靠惯常稀散近似免费支付的中间区间。

本文只给有限模型的精确约化嵌入及常数量词等价；没有据此完成一般正性、原 graph 返回控制或普通 Hilbert 不变子空间问题。
