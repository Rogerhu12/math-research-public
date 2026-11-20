# R654：完整双积分空间的 H² 等价尺度、端口谱界与同范数增广

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence。

**状态：已证明。** 本文给出有限共享 quintic 空间上的准确实数定理：完整双积分坐标的第二缺陷必须以 $D/h$ 衡量，才能与胞内真实二阶导数具有网格一致的范数等价；对应双端口矩阵的对角归一化谱界不依赖最小胞宽或最大角模；在同一范数中白化的粗空间不会任意削弱步范数。并完整核对此前 L² 尺度的端口谱界。本文不把正定性、预条件或某次目标下降解释为闭合等距解、连续曲率界、reach 或本课题完成。

## 1. 实际完整坐标与端口

设 $0=s_0<\cdots<s_{J-1}=S$，$h_i=s_{i+1}-s_i>0$，$J\ge2$。每节点有 $n=3M+2$ 个旋转架系数的三 jet $(Y_j,U_j,A_j)$。系数次序为

$$
R_0,\ldots,R_M;\quad T_1,\ldots,T_M;\quad Z_0,\ldots,Z_M.
$$

$R_j,T_j,Z_j$ 的角频率为 $\nu=2j$，令 $\lambda_k=\sqrt{1+\nu_k^2}$。固定前 $K$ 个 core 系数，只保留 $c_j$, $K<j\le M$ 的变化。以下先写齐次切向空间；仿射固定项最后补回。

入口为 $U_0=0$，$Y_0=C(c)$，其中

$$
C_{R_j}=c_j,\qquad C_{T_j}=-\nu_jc_j\quad(j>K),
$$

其余入口系数为零。自由加速度是 $A_0$ 的全部 R/T 槽及所有内部节点 $A_1,\ldots,A_{J-2}$；$A_{0,Z}=0$，$A_{J-1}=0$ 准确固定。每胞、每个系数的两种缺陷均保留：

$$
E_i={U_{i+1}-U_i\over h_i}-{A_i+A_{i+1}\over2},
\qquad
D_i={Y_{i+1}-Y_i\over h_i}-{U_i+U_{i+1}\over2}. \tag{1}
$$

另有完整解析 lift 的高度参数 $H$。坐标向量记为 $x=(c,A_{\rm free},E,D,H)$。反向递推是

$$
U_{i+1}=U_i+h_i\{(A_i+A_{i+1})/2+E_i\},\quad
Y_{i+1}=Y_i+h_i\{(U_i+U_{i+1})/2+D_i\}. \tag{2}
$$

给定全节点三 jet，式 (1) 唯一给出 E、D；给定 x，式 (2) 唯一重建全节点三 jet。因此这只是可逆坐标变换，胞内仍用同一个共享 quintic Hermite 插值，并未令 E 或 D 为零。

令

$$
t_i=S-{s_i+s_{i+1}\over2},\quad
w_j={1\over2}\sum_{i:\,j\in\{i,i+1\}}h_i,\quad
v_j={1\over2}\sum_{i:\,j\in\{i,i+1\}}h_it_i. \tag{3}
$$

对 (2) 的有限和交换求和次序，得到完整末端算子

$$
Bx=\binom{U_{J-1}}{Y_{J-1}}
=\binom{\sum_jw_jA_j+\sum_ih_iE_i}
 {C(c)+\sum_jv_jA_j+\sum_ih_it_iE_i+\sum_ih_iD_i}. \tag{4}
$$

具体地，每个增量 $\Delta U_i$ 对 $Y_{J-1}$ 的权为
$\frac12h_i+\sum_{\ell>i}h_\ell=S-(s_i+s_{i+1})/2=t_i$，故 (4) 包含非均匀网格的全部端点半胞项。固定入口 P、C 的仿射情形只增加 $(P,C_{\rm fixed}+SP)$，不改变 B 或下面的 Gram。

任取一个胞 i、一个系数 k，单独选择 $E_{ik}=u/h_i$、$D_{ik}=(y-t_i u)/h_i$，其端口是任意指定的 $(u,y)$。因此 B 的秩准确为 2n。x 的维数为 $(3J-3)n-K$，约束 $Bx=0$ 后维数 $(3J-5)n-K$，等于原 fullclosed 自由空间。H 的端口列为零。式 (1)、(2) 在此约束空间与原自由三 jet 间互逆。

## 2. 两个明确的正尺度

设固定 lift 宽度 $\ell>0$。仅对实际存在的自由槽定义正对角矩阵 $\mathcal S_r$，其中 $r=0$ 是原 L² 缺陷尺度，$r=2$ 是本次 H² 型尺度：

| 坐标 | $\mathcal S_0$ | $\mathcal S_2$ |
|---|---:|---:|
| 自由 core $c_j$ | $\lambda_j^{-2}$ | $\lambda_j^{-2}$ |
| 自由 $A_{jk}$ | $(\sqrt{w_j}\lambda_k)^{-1}$ | 同左 |
| 全部 $E_{ik}$ | $(\sqrt{h_i}\lambda_k)^{-1}$ | 同左 |
| 全部 $D_{ik}$ | $(\sqrt{h_i}\lambda_k)^{-1}$ | $\sqrt{h_i}/\lambda_k$ |
| $H$ | $\ell$ | $\ell$ |

H² 尺度恰是把原 D 尺度乘以各自的 $h_i$，没有删除自由度。坐标范数为

$$
\begin{aligned}
\mathcal N_0(x)^2={}&\sum_{j>K}\lambda_j^4c_j^2+H^2/\ell^2\\
&+\sum_k\lambda_k^2\left\{\sum_{j\ {
m free}}w_jA_{jk}^2+
\sum_ih_i(E_{ik}^2+D_{ik}^2)\right\},\\
\mathcal N_2(x)^2={}&\sum_{j>K}\lambda_j^4c_j^2+H^2/\ell^2\\
&+\sum_k\lambda_k^2\left\{\sum_{j\ {
m free}}w_jA_{jk}^2+
\sum_ih_i E_{ik}^2+\sum_i{D_{ik}^2\over h_i}\right\}.
\end{aligned} \tag{5}
$$

它们准确等于 $\|\mathcal S_r^{-1}x\|_2^2$。固定为零的 A 槽可加入求和而不改变数值。这里是系数范数，尚未声称等于完整几何面的弯曲能量；R/T 的旋转架、完整解析 lift 与非线性第一基本形式仍按原物理算子处理。

## 3. H² 尺度与真实胞内二阶导数的统一等价

### 命题 1

令 q 为一个胞 $[s_i,s_{i+1}]$ 上由六个端点 jet 决定的任意标量 quintic。令 $h=h_i$、$u=(s-s_i)/h$，并用 (1) 定义 E、D。则

$$
{1\over11}\left\{{h\over2}(A_i^2+A_{i+1}^2)+hE^2+{D^2\over h}\right\}
\le\int_{s_i}^{s_{i+1}}|q''(s)|^2\,ds
\le18\left\{{h\over2}(A_i^2+A_{i+1}^2)+hE^2+{D^2\over h}\right\}. \tag{6}
$$

常数对所有 h、所有端点值及所有非均匀网格一致。

**证明。** 设 $v(u)=q''(s_i+hu)$，为次数不超过三的多项式，$a=A_i$、$b=A_{i+1}$、$d=D/h$。由两次积分和 (1)，

$$
v(0)=a,\quad v(1)=b,\quad
\int_0^1v(u)\,du=(a+b)/2+E,\quad
\int_0^1(1/2-u)v(u)\,du=d. \tag{7}
$$

解这四个线性条件，得到唯一的完整 cubic

$$
\begin{aligned}
v(u)={}&a(1-6u+15u^2-10u^3)+b(6u-15u^2+10u^3)\\
&+E(6u-6u^2)+d(60u-180u^2+120u^3). \tag{8}
\end{aligned}
$$

直接对四个明确多项式的两两乘积积分，令 $\theta=(a,b,E,d)^T$，则

$$
\int_0^1v^2\,du=\theta^TG_*\theta,\qquad
G_*=\begin{pmatrix}
2/7&3/14&1/2&-3/7\\
3/14&2/7&1/2&3/7\\
1/2&1/2&6/5&0\\
-3/7&3/7&0&120/7
\end{pmatrix}. \tag{9}
$$

取 $W=\operatorname{diag}(1/2,1/2,1,1)$。展开行列式，

$$
\det(G_*-tW)={(5t^2-11t+1)(7t^2-121t+12)\over140}.
$$

所以 $W^{-1/2}G_*W^{-1/2}$ 的四个特征值准确为

$$
{11\pm\sqrt{101}\over10},\qquad
{121\pm\sqrt{14305}\over14}. \tag{10}
$$

较小的两根可分别写成 $2/(11+\sqrt{101})>1/11$、
$24/(121+\sqrt{14305})>12/121>1/11$；较大的两根均小于 18。因此 $W/11\preceq G_*\preceq18W$。乘以 $ds=h\,du$ 得 (6)。这同时证明 (7) 的四量完整决定 cubic，且 Gram 严格正定。证毕。

对每个角系数 k 乘 $\lambda_k^2$，对所有胞求和。共享节点每次出现的半胞权之和正是 (3) 的 w；故

$$
{\mathcal A_2(x)^2\over11}
\le\sum_k\lambda_k^2\int_0^S|q_k''(s)|^2\,ds
\le18\mathcal A_2(x)^2,\qquad
\mathcal A_2^2=\sum_k\lambda_k^2\left(\sum_jw_j A_{jk}^2+\sum_i h_iE_{ik}^2+\sum_iD_{ik}^2/h_i\right). \tag{11}
$$

再加入 (5) 相同的非负 core 与 H 项，得到整个 $\mathcal N_2^2$ 与“加权 $q''$ 的平方积分 + 同 core/H 项”之间同一组 $1/11,18$ 常数。它控制完整 polynomial 部分，绝非只控制节点加速度。

原 $\mathcal N_0$ 不具此网格一致控制：取两个相邻等宽胞 h，全部 U、A 为零，Y 只在共同中点节点取 $hd$，其余节点为零，core/H 为零。此方向保持全部入口、末端和共享 C² 条件；两胞 E=0，D 分别为 d、−d。由 (9)，$\int|q''|^2=240d^2/(7h)$，而原缺陷平方范数为 $2hd^2$，两者之比 $120/(7h^2)\to\infty$。这说明 D 的额外 h 因子是二阶导数量纲所需，原 L² 端口条件良好本身不能防止胞内曲率放大。

## 4. 原 L² 与新 H² 端口 Gram 的完整谱界

令 $G_r=B\mathcal S_r^2B^T$。由 (4)，在任一系数 k 的端口次序 $(U_k,Y_k)$ 下，先不计 free core 列，准确小块为

$$
\begin{pmatrix}
\sum_{j\ {\rm free}}w_j^2(s^A_{jk})^2+\sum_i h_i^2(s^E_{ik})^2 &
\sum_{j\ {\rm free}}w_jv_j(s^A_{jk})^2+\sum_i h_i^2t_i(s^E_{ik})^2\\
\text{同上} &
\sum_{j\ {\rm free}}v_j^2(s^A_{jk})^2+\sum_i h_i^2t_i^2(s^E_{ik})^2+\sum_i h_i^2(s^D_{ik})^2
\end{pmatrix}. \tag{12}
$$

R/T 的自由 A 节点是 $0,\ldots,J-2$；Z 的是 $1,\ldots,J-2$。这正包括真实 A 入口权和省去的固定槽，不能一律替成内部节点权。

令 $H_3=\sum_i h_i^3$。逐胞对 $(S-s)^2$ 作准确中点积分可得

$$
\sum_i h_i=S,\quad \sum_i h_it_i=S^2/2,\quad
U:=\sum_i h_it_i^2=S^3/3-H_3/12,\quad 0<H_3\le S^3. \tag{13}
$$

最后一个不等式由正数求和的立方展开立即得到，因而 $S^3/4\le U\le S^3/3$。

### 原 L² 尺度

把 (12) 乘 $\lambda_k^2$，E/D 单独给出

$$
G_{ED,0}=\begin{pmatrix}S&S^2/2\\S^2/2&S+U\end{pmatrix}.
$$

其行列式至少为 $S^2$，迹至多为 $2S+S^3/3$。对 2×2 正定矩阵，$\lambda_{\min}=\det/\lambda_{\max}\ge\det/\operatorname{tr}$，所以

$$
\lambda_{\min}(G_{ED,0})\ge a_0:={S\over2+S^2/3}. \tag{14}
$$

A 的贡献为正半定和 $\sum_{j\ {\rm free}}w_j^{-1}(w_j,v_j)(w_j,v_j)^T$。由 $0\le v_j\le Sw_j$、$\sum_jw_j=S$，其迹至多 $S+S^3$。因此不计 core 时总块上界是 $(3S+4S^3/3)I$。

### 新 H² 尺度

此时 D 给出右下元 $\sum_i h_i^3=H_3$，故

$$
G_{ED,2}=\begin{pmatrix}
S&S^2/2\\S^2/2&S^3/3+11H_3/12
\end{pmatrix}. \tag{15}
$$

准确行列式为 $S^4/12+11SH_3/12\ge S^4/12$，迹至多 $S+5S^3/4$。于是

$$
\lambda_{\min}(G_{ED,2})\ge a_2:={S^3\over12+15S^2}. \tag{16}
$$

加入同一 A 正半定和后，上界为 $(2S+9S^3/4)I$。

### 真实 free core 的 4×4 配对

每个自由 core 模 j 同时改变 $Y_{R_j},Y_{T_j}$。在次序 $(U_R,Y_R,U_T,Y_T)$ 中，它贡献

$$
\lambda_j^{-4}qq^T,\qquad q=(0,1,0,-\nu_j)^T. \tag{17}
$$

R/T 两块有相同 $\lambda_j$。乘以 $\lambda_j^2$ 后，(17) 唯一非零特征值为
$\lambda_j^{-2}\|q\|^2=(1+\nu_j^2)/\lambda_j^2=1$。所以这是一个非负、范数恰为 1 的更新；固定 core 只进仿射常数，没有此列。H 没有端口列，也不产生额外块。

据此置

$$
b_0=3S+4S^3/3+1,\qquad b_2=2S+9S^3/4+1. \tag{18}
$$

对 r=0 或 2 的每个完整 2×2 或 4×4 块 $G_{r,\mathcal I}$，都有

$$
{a_r\over\lambda_{\mathcal I}^2}I
\preceq G_{r,\mathcal I}
\preceq{b_r\over\lambda_{\mathcal I}^2}I. \tag{19}
$$

各自由 core 配对占 4 行，其余每系数占 2 行，恰好互不重复地覆盖全部 2n 行。

令 $D_G=\operatorname{diag}(G_r)^{1/2}$。由 (19)，各块对角元亦介于同一上下界；代入二次型可得

$$
{a_r\over b_r}I\preceq D_G^{-1}G_rD_G^{-1}
\preceq{b_r\over a_r}I,\qquad
\kappa_2(D_G^{-1}G_rD_G^{-1})\le(b_r/a_r)^2. \tag{20}
$$

每块归一化后的区间相同，因此 (20) 既对单块成立，也对全部 2n 行的归一化直和成立。常数只依赖固定总长 S，不依赖 $\min h_i$、J、M、K、自由 A 端点槽多少或角频率；未归一化矩阵仍有 $\lambda^{-2}$ 模间尺度，本文不把它的条件数误写为模数一致。

## 5. 完整端口投影与保留全部原自由方向

取任一 r，令 $K_r=B\mathcal S_r$，

$$
\Pi_r=I-K_r^TG_r^{-1}K_r. \tag{21}
$$

上节已证明 $G_r$ 正定，又 $K_rK_r^T=G_r$，直接相乘给出 $\Pi_r^T=\Pi_r$、$\Pi_r^2=\Pi_r$、$K_r\Pi_r=0$。故它是到 $\ker K_r$ 的欧氏正交投影。

记 T 为 (2) 的完整三 jet 重建，Extract 取原自由槽，则

$$
L_r=\operatorname{Extract}\,T\mathcal S_r\Pi_r,
\qquad
L_r^T=\Pi_r\mathcal S_rT^T\operatorname{Extract}^T. \tag{22}
$$

由于 (1)、(2) 在端口子空间上互逆，$L_r$ 限于 $\operatorname{ran}\Pi_r$ 是到原自由空间的双射。给原自由方向 b，其唯一最小欧氏长度表示是

$$
u=\mathcal S_r^{-1}\operatorname{Inverse}(b;\ {
m tangent}),\qquad
u\in\operatorname{ran}\Pi_r,\quad L_ru=b. \tag{23}
$$

任一其他表示与 u 之差在 $\ker\Pi_r$，与 u 正交。完整仿射端口的修复则为

$$
x\longmapsto x-\mathcal S_r^2B^TG_r^{-1}(Bx+b_{\rm fixed}). \tag{24}
$$

这里没有删掉 E、D、core 或高度。物理 Gram 行、角行重数、$\rho,\Theta$ 与解析 lift 的原链式导数均保持在原 J 中；新线性方向算子是 $JL_r$，其伴随是 $L_r^TJ^T$。只有步正则范数改变。

## 6. 同范数白化粗空间只能把平方步范数减少至一半

设 C 为任意线性独立、满足原完整端口的有限粗方向列。按 (23) 逐列取

$$
Z_{\rm raw}=\mathcal S_2^{-1}\operatorname{Inverse}(C;\ {
m tangent}),\quad
G_C=Z_{\rm raw}^TZ_{\rm raw}.
$$

双射保证 $G_C$ 正定。取 $R^TG_CR=I$，例如若 $G_C=LL^T$ 则 $R=L^{-T}$。令 $Z=Z_{\rm raw}R$、$\widehat C=CR$。于是

$$
Z^TZ=I,\quad \Pi_2Z=Z,\quad \widehat C=L_2Z. \tag{25}
$$

对任一原方向 b，令 u 为 (23) 的最小表示。使用增广算子 $[L_2,\widehat C]$ 时，其最小平方系数范数为

$$
\begin{aligned}
\min_{L_2a+\widehat C d=b}(\|a\|^2+\|d\|^2)
&=u^T(I+ZZ^T)^{-1}u\\
&=\|u\|^2-\tfrac12\|Z^Tu\|^2
\in[\tfrac12\|u\|^2,\|u\|^2]. \tag{26}
\end{aligned}
$$

证明是先去掉 a 在 $\ker\Pi_2$ 的无用分量，约束遂变为 $a+Zd=u$。代入 $a=u-Zd$ 并配方，最优 $d=Z^Tu/2$，即 (26)。若粗列相关，先取其实际列空间的任意基即可；完整 L₂ 仍保留所有原自由方向。

因此额外的粗方向不会因其物理 Gram 导数很弱而任意绕过 H² 范数。这里白化的是 (5) 的坐标范数，不能以 $\|JC_j\|$ 的列均衡替代。可按系数通道累加精确有限矩阵

$$
G_C=\sum_k\lambda_k^2\{A_k^T\operatorname{diag}(w)A_k+
E_k^T\operatorname{diag}(h)E_k+D_k^T\operatorname{diag}(h^{-1})D_k\}
+\sum_{j>K}\lambda_j^4 c_j^Tc_j+H^TH/\ell^2, \tag{27}
$$

其中各矩阵的列就是粗方向，E/D 按 (1) 计算；不存在的 A 槽为零。式 (27) 不要求建立全自由维数乘粗列数的大矩阵。式 (26) 是数学范数结论，不给出任何非线性收敛率或具体线性求解迭代数。

## 7. 同一 C² 方向随网格精化不会遭受人为发散的惩罚

固定有限个角模和满足上述端口的一个 C² 系数函数 q，把它的准确三 jet 限制到任意 $h_{\max}\to0$ 的网格。写 $A=q''$，$\omega_A$ 为其连续模。E 是 A 的积分均值减端点均值，所以 $|E_i|\le\omega_A(h_i)$。两次积分还给出

$$
D_i={1\over h_i}\int_{s_i}^{s_{i+1}}(m_i-s)A(s)\,ds,
\quad m_i=(s_i+s_{i+1})/2.
$$

权 $m_i-s$ 的积分为零，减去 $A(m_i)$，得

$$
|D_i|\le{h_i\over4}\omega_A(h_i/2),\qquad
\sum_i{D_i^2\over h_i}\le{S\over16}\omega_A(h_{\max}/2)^2\longrightarrow0. \tag{28}
$$

又 $\sum_i h_iE_i^2\le S\omega_A(h_{\max})^2\to0$，而 $\sum_jw_jA(s_j)^2\to\int_0^SA(s)^2ds$ 是连续函数的非均匀梯形和。因此 $\mathcal N_2^2$ 收敛到同 core/H 项加 $\sum_k\lambda_k^2\int|q_k''|^2$，无需 q 为 C³。原 $\mathcal N_0^2$ 对固定 C² 方向也有这个极限，但第 3 节的两胞反例说明，它不能统一控制随网格改变的所有离散方向。这两项陈述并不矛盾。

## 8. 与原实现逐项绑定及适用边界

原完整实现是 [DoubleIntegrated 源码](../notes/2026-11-17-parallel-root-fullclosed-integrated-coordinates.py)，SHA-256 `d429d68baded58908454e49f4bfdf8e43ce9d3f857ed666eafa95c1c366462db`，Git blob `f4effeb788f156c7fdc2e260db54b06a91f976e1`；此前的完整坐标说明见[原证明](../notes/2026-11-17-parallel-root-fullclosed-double-integrated-coordinates.md)。本次检查的对应关系为：

| 原方法或数据 | 本文中的完整对象 |
|---|---|
| `_parts` 的 A0 水平槽、内部 A、全部 E/D | 第 1 节真实自由槽；A0Z、末端 A 固定零 |
| `w`, `v`, `t` | (3) 的非均匀权，含两个端点的半胞项 |
| `raw`, `inverse` | 完整递推 (2) 及真实缺陷 (1) |
| `endpoint`, `endpoint_transpose` | (4) 的 B、Bᵀ；仿射 offset 独立 |
| `_gram_blocks` | (12) 加 (17)，自由 core R/T 为 4×4，其余为 2×2 |
| `project`, `lift`, `pullback`, `repair` | (21)、(22)、(24)；lift/pullback 内已含尺度 |

原 [L² 尺度 helper](../scripts/integrated_l2_scale_20261120.py) 的 SHA-256 为 `ff147637f4d5ebc52700e0ee58ba168374fb86ff72f641ae004ba67e2eb5c560`，准确实现表中 $\mathcal S_0$。[本次 H² LM 源](../scripts/resume_20261120/fullclosed_integrated_h2_lm.py) 的 SHA-256 为 `861a9de1a1ae9859cae0adcc813de3f4f76d656c7f9e48821b3069ec483f02c6`；它只把该尺度向量的完整 D 分段逐胞乘 h，得到 $\mathcal S_2$，并在相同范数中白化粗列。

以上证明是已写明有限矩阵的准确实数命题，不把浮点 Cholesky、回代或端口投影的残余称为严格零，也不把 (20) 当成 IEEE 舍入误差证明。证明不依赖某次旧数值比较是否过阈值，没有新设科学验收条件。真实步长、实际非线性目标、连续同 g 精化、胞内曲率、闭面与全局 reach 仍由对应实际问题决定。
