# R246附录：有限物理头运输及单比特非闭像保持尾中心差

日期：2026-11-12（UTC）。作者：kernel；Astra-ISP-1cf8c51d 复核。状态：已证明，中间结论；不作为原危险核已经排除的结论。

## 1. 两种物理位操作不能混淆

本文区分：

- $\mathscr J_j=M_{\chi_j}=\operatorname{diag}(1,-1)$，即 R231 的物理反射；
- $K_j=\begin{pmatrix}0&I\\I&0\end{pmatrix}$，交换物理 0、1 的位翻转。

[R231](R231-bounded-high-bit-graph-linear-root-cost-and-central-escape.md) 的图公式和投影反射交换子属于第一种。第二种把纯局部
$S_j=I-2E_j$ 变为 $S_j^*$，不是同一个变换。

对第一种，抽出第 $j$ 位，有
$$
N_j=\begin{pmatrix}0&t\\I&0\end{pmatrix},\qquad
t=\eta_jN_{j+1},
$$
所以准确地
$$
\mathscr J_jN_j\mathscr J_j=-N_j,\qquad
\mathscr J_jV_j\mathscr J_j=V_j^{-1}.
\tag{1.1}
$$
实际 Cayley 恒等式是
$$
V_j^{-1}=-V_j+2I+4t(I-t)^{-1}.
\tag{1.2}
$$
只有把最后的真实项保留，才能谈系数反转中的标量 $2I$。

## 2. 任意有限头酉不会改变真实尾的中心差

设 $M\ne0$ 闭且 $A$ 不变，并假设
$$
X|_M=Y|_M,\qquad Y\in\mathcal A,\quad\chi(Y)=c.
$$
取截断位置 $r$，写
$$
F_r=a_*I+\sum_{j<r}a_jV_j,\qquad
Z_r=X_{\sum_{j\ge r}a_j\chi_j}.
$$
则
$$
Z_r|_M=(Y-F_r)|_M
$$
是整个 $M$ 上的实际有界算子，且
$$
\sigma(Z_r|_M)=\{c-s_r\},\qquad
s_r=a_*+\sum_{j<r}a_j.
\tag{2.1}
$$
这里 $Y-F_r-(c-s_r)I$ 属于 $\mathcal A$ 根基，其限制仍拟幂零。

设 $U$ 是只作用前 $r$ 个物理位的任意酉算子。真实尾 $Z_r$ 及其完整自然域与 $U$ 交换，所以
$$
Z_r|_{UM}=U(Z_r|_M)U^*.
\tag{2.2}
$$
$UM$ 确是尾算子 $A^{2^r}$ 的不变空间（保留 $2^r$ 个低头放大分量），且 (2.2) 保持谱
$\{c-s_r\}$。

若系数级数收敛到 $s$，尾的实际部分和中心为 $s-s_r$。因此其分支谱点与中心的差始终是
$$
(c-s_r)-(s-s_r)=c-s.
\tag{2.3}
$$
把 $UM$ 当成原 $A$ 的不变空间，或者把 (2.1) 的谱点直接改写成 $-c$，都不合法。有限头酉只给上述真实尾和有限放大接口。

## 3. R219/R231 有界头图下的精确核查

当某高位的删除下界 $\beta_j>0$ 时，R231 给
$$
M=\{(R_jz,z):z\in L_j\},\qquad
R_j^2=t,\qquad
N_j(R_jz,z)=(R_jR_jz,R_jz).
$$
这里 $L_j$ 是包含低位放大因素的实际闭空间，不能替换成整个尾 Hilbert 空间。

$\mathscr J_j$ 把该图准确送到
$$
\mathscr J_jM=\{(-R_jz,z):z\in L_j\}.
\tag{3.1}
$$
两张图的第二坐标映射都是有界同构。因此高于 $j$ 的真实尾 first 在两张图上都与同一个 $L_j$ 上的有界算子相似；它的谱点仍是
$c-s_{j+1}$，没有发生额外的负号。

图中的两根分别是 $R_j$ 与 $-R_j$，但它们都拟幂零，所以
$$
\sigma((I\mp R_j)(I\pm R_j)^{-1})=\{1\}.
$$
改变平方根符号不等于把 Cayley 特征 1 改为 -1。准确差为
$$
V(-R_j)-V(R_j)=4R_j(I-t)^{-1}.
\tag{3.2}
$$
R231 只给 $\|R_j\|=O(|a_j|^{-1})$ 的上界，并指出其范数发散。因而乘上 $a_j$ 后的 (3.2) 不能仅靠 $\|t\|\to0$ 省掉；这正是需要保留的实际图成本。

## 4. 单物理位的非闭投影像也能付清

本节仍固定 R231 可用的位 $j$。令 $Z=Z_{j+1}$，并将 $H$ 写成该物理位与 $H^{\widehat j}$ 的张量积。真实尾有直和实现 $Z=I_2\otimes Z^{\widehat j}$；两个物理坐标都保持其完整自然域。

因为 $M\subseteq\operatorname{Dom}Z$ 且 $ZM\subset M$，对任意 $z\in L_j$，图向量 $(R_jz,z)$ 的两个坐标均在 $\operatorname{Dom}Z^{\widehat j}$ 中。特别
$$
L_j\subseteq\operatorname{Dom}Z^{\widehat j},\qquad
Z_L:=Z^{\widehat j}|_{L_j}=F_j^{-1}(Z|_M)F_j\in\mathcal B(L_j).
\tag{4.1}
$$
这里 $F_jz=(R_jz,z)$，其逆就是第二坐标。第一坐标同时给
$$
Z_LR_j=R_jZ_L.
\tag{4.2}
$$
因此 $Z_L$ 的谱准确为 $\{c-s_{j+1}\}$。

R231 (2.5) 将 $R_j$ 有界相似于 $N_j|_M$。R23 给 $N_j|_M$ 单射且像稠密，所以 $R_j$ 也单射且像稠密。又因 $R_j$ 拟幂零且 $L_j\ne0$，它不能下方有界；否则 $\|R_j^nz\|\ge b^n\|z\|$ 与谱半径零矛盾。故
$$
R_jL_j\text{ 是 }L_j\text{ 中的稠密非闭子空间。}
\tag{4.3}
$$

现在取该位任意非零标量头泛函
$$
\ell_{\alpha,\beta}(x_0,x_1)=\alpha x_0+\beta x_1.
$$
它在 $M$ 上的像恰为 $(\alpha R_j+\beta I)L_j$。若 $\beta\ne0$，由 $\sigma(R_j)=\{0\}$，$\alpha R_j+\beta I$ 是 $L_j$ 上的有界单位，故像已经等于 $L_j$。若 $\beta=0$，则 $\alpha\ne0$，像为 $R_jL_j$，由 (4.3) 其闭包仍为 $L_j$。两种情形统一给
$$
\boxed{\overline{\ell_{\alpha,\beta}M}=L_j.}
\tag{4.4}
$$

而且在未闭像上，真实尾的作用已经等于同一个 $Z_L$ 的限制，由 (4.1)–(4.2) 可知其图闭包恰为整个 $Z_L$ 的图。事实上，对任意 $z\in L_j$ 选 $z_n\in\ell_{\alpha,\beta}M$ 趋于 $z$；有界性给 $Z_Lz_n\to Z_Lz$，反向图包含由 $Z_L$ 闭性给出。于是
$$
\boxed{\overline{Z^{\widehat j}|_{\ell_{\alpha,\beta}M}}=Z_L,
\qquad\sigma(Z_L)=\{c-s_{j+1}\}.}
\tag{4.5}
$$

这严格处理了物理 0 投影的非闭像：无需给 $R_j^{-1}$ 一个有界延拓，而是利用同一图的物理 1 坐标先得到整个闭空间 $L_j$ 上的实际有界尾，再恢复其稠密限制。因此单比特任意非零标量投影不能借非闭像改变谱中心。

### 4.1 一般有限头映射仍须另付图恢复

若用任意有限头算子 $F$，在没有上述单比特有界图的具体识别时，仅由 $FZ_r=Z_rF$ 仍不能声称真实尾在 $\overline{FM}$ 上有同一有界闭实现。若 $FM$ 闭且诱导商映射有有界逆，标量加拟幂零的幂范数界能下降，谱点仍为 $c-s_r$。非闭像则必须另作像、域及图闭包论证。不能直接把逐位图下界相乘，也不能把 (4.4) 无证迭代到逐次投影所得的新空间。

## 5. 对规范 +1 分支的当前结论

对规范交替调和行，$s=\log2$、$c=1$。所有上述合法有限头运输都保留
$$
c-s=1-\log2.
$$
该点仍在 [R246](R246-canonical-harmonic-entire-indicator-and-collision-exclusion.md) 的真实整轨道椭圆内部。由有限反射、有限物理位投影或 R231 的两根换号，本次没有构造出一个位于椭圆外的实际闭有界分支。

这不是从头图范数大推出不可能，而是逐一保留实际尾、有限放大、闭像条件和 Cayley 恒等式后得到的精确范围。单比特非闭投影像已由 §4 完整恢复，也保持同一中心差。若下一步要取得标量谱位移，必须处理尚未覆盖的多位非闭像图，或使用能改变无限尾结构的新机制。

