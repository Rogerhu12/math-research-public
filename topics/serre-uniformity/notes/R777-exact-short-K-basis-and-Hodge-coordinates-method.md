# R777 原 K 基的准确短展开与 Hodge 立方坐标：公开执行方法

日期：2026-11-14。状态：**运行前方法；不预称本阶段已返回结果。**

本阶段直接计算 R775 实际选定的原 $K$ 基的特征零系数，并将 R774 已完成的原 $H^3$ 写成实际权六基的 $L$ 线性组合。最终产物是全部原权六、权十二基的 $q_Y^0,\ldots,q_Y^{142}$ 准确展开，以及一个经有理矩阵恒等式认证的原 $H^3$ 坐标列。真正 $A/B$ 的恢复随后使用这些实际数据和全部 143 个原 Laurent 条件；本阶段不把辅助素数的核或理论维数登记为函数。

R775 的实际 producer 只有在公开成功之后才能填入请求。请求中的 `producer_inputs_pending` 必须为 false，且同时绑定其真实 run/source、artifact ID/ZIP SHA、manifest、小证书和核心 SHA。没有预填的成功结果或猜测哈希。未齐输入的稿暂存于 `notes/R777-public-exact-short-K-basis-pending.json`；该路径不触发 workflow。真实 R775 成功后，才把完整绑定写入最终 `-request.json` 并触发实际计算。

## 1. 同一原模型、同一算术基及短注入界

固定原
$$
K=\mathbf Q(\zeta)=\mathbf Q(s),\quad s=1+2\zeta,\quad s^2=-3,\quad
L=K(b),\quad M=L(\xi),\quad \xi=e^{2\pi i/41}.
$$
原参考参数保持
$$
Q=e^{2\pi i\tau/246},\qquad u=q_Y=Q^3=e^{2\pi i\tau/82},
\qquad \xi_{82}=-\xi^{21}.
\tag{777.1}
$$
原 $c_1=4424$、原 $6^{-1}$ Fourier 相位与实际微分都不重新运输。这里仍在参考 cusp 展开。

R775 的每个原 $K$-定义权二基都有实际 recipe
$$
T_{j,r}=\sum_{d\in(\mathbf Z/82)^\times}
 \xi_{82}^{jd}(B_r*g_d),\qquad
B_r=\frac12\sum_{h\in H_{82}}E_{\lambda_rh}E_{\mu_rh}.
\tag{777.2}
$$
原 $|H_{82}|=252$，由于两个权一形式同时取负，半迹可恰好写成原 $H_{82}/\{\pm I\}$ 的 126 项。$g_d$ 是 R775 已保存的实际行列式代表，其 $d$ 指模 82 的奇数提升，不能换成裸的模 41 整数。

本阶段只读取真正被 R775 选中的 recipe、主元证书和有限域系数，不再选基。它按同一个 recipe 生成第一次出现的准确系数。原 R771 已保存的群、E1 模 739 表与 level-one 模表也直接读取。

R778 已证明原二十 cusp 在 $L$ 上构成一个 Galois 轨道，且原完整 $\xi$ 坐标的以下展开映射单射：
$$
M_6(Y/L)\longrightarrow
 \bigoplus_{0\le n\le41}M\,u^n,
\qquad
M_{12}(Y/L)\longrightarrow
 \bigoplus_{0\le n\le82}M\,u^n.
\tag{777.3}
$$
权六线丛次数为 820，故 $20\cdot42=840>820$；权十二的次数为 1640，故 $20\cdot83=1660>1640$。它们使用 $L$ 定义性和完整 cusp 系数，不能以单个数值嵌入替代。

R774 真正完成的原立方 $\mathcal H=H^3$ 在 $M_6(Y/L)$ 中，原实际 $e=1$。因此它在 $q_Y^0,\ldots,q_Y^{41}$ 的准确坐标已足以解其全局权六表达。本阶段直接读取这部分原输出，不重新立方或扩展旧微分。

## 2. 整数 E1 展开的准确常数项

记 $E_{a,b}$ 为 Zywina Lemma 4.7 的同一权一 Eisenstein 形式，$0\le a,b<82$。正阶项为
$$
E_{a,b}=c_{a,b}+
 \sum_{\substack{m,n\ge1\\m\equiv a\ (82)}}\xi_{82}^{bn}u^{mn}
 -
 \sum_{\substack{m,n\ge1\\m\equiv-a\ (82)}}\xi_{82}^{-bn}u^{mn}.
\tag{777.4}
$$
当 $a\ne0$，
$$
82c_{a,b}=41-a.
\tag{777.5}
$$
当 $a=0,b\ne0$，置 $z=\xi_{82}^b$、$m=\operatorname{ord}(z)\mid82$。由
$$
\sum_{k=0}^{m-1}kz^k=-\frac m{1-z},
$$
得到
$$
82c_{0,b}
=82\frac{1+z}{2(1-z)}
=-\frac{82}{m}\sum_{k=0}^{m-1}kz^k-41.
\tag{777.6}
$$
$(a,b)=(0,0)$ 单独取零；不能在 (777.6) 中令 $z=1$。

因此
$$
\boxed{82E_{a,b}\in\mathbf Z[\xi][[u]].}
\tag{777.7}
$$
所有正阶项只是带符号的 $82\xi_{82}^j$；用
$\xi_{82}^j=(-1)^j\xi^{21j}$ 可以准确写入 41 个循环坐标。常数项 (777.6) 也是有限整数和，无需在数域中做反演或根据模 739 值猜测有理数。

程序把每个第一标签 $a$ 的全部 82 个准确 E1 短展开保存为一个独立阶段。第一次产生时，按原 $\xi\mapsto538$ 把它除以 82 后与 R771 已有模表的全部 $0\le n\le142$ 比较。完成行直接恢复，不重新生成。

## 3. 携权的行列式迹及全部重数

对一个真正用到的 R771 种子 $r$ 和 R775 代表 $g_d$，准确计算
$$
82^2(B_r*g_d)
=\sum_{h\in H_{82}/\{\pm I\}}
 (82E_{\lambda_rhg_d})(82E_{\mu_rhg_d}).
\tag{777.8}
$$
程序按乘法交换性合并重复的标签对，但保留整数重数；总重数始终为 126。每个已完成的 $(r,d)$ 独立保存。

再依照 (777.2) 乘原 $\xi_{82}^{jd}$，其中 $d$ 是已保存的 `det_mod82`。在 41 个循环坐标中，这恰是乘 $(-1)^{jd}$ 并循环平移 $21jd$，不能省去符号。汇总全部四十个代表后，以
$$
\Phi_{41}(\xi)=0
$$
消去最后一个坐标，得到 $1,\xi,\ldots,\xi^{39}$ 的准确系数。于是
$$
\widetilde T_{j,r}:=82^2T_{j,r}\in\mathbf Z[\xi][[u]].
\tag{777.9}
$$
每个选中的 $\widetilde T_{j,r}$ 都逐系数核对其模 739 值是否等于原 R775 对应基行乘 $82^2$。这只核对同一已选 recipe 和相位；特征零系数本身来自 (777.4)–(777.8)。

## 4. 原低权乘积与统一 82 的幂尺度

R775 的普通乘积 recipe 是原权二基之间的真实乘积。若其权为 $2k$，统一保存
$$
82^{2k}F\in\mathbf Z[\xi][[u]].
\tag{777.10}
$$
每个因子的 $\xi$ 次数至多 39。用
$$
u^n\xi^r\longmapsto Z^{79n+r}
\tag{777.11}
$$
作准确整数低乘，因为 $39+39=78<79$，没有跨 $u$ 块进位。保留 $Z$ 次数小于 $79\cdot143$ 后，对每个块先按 $\xi^{41}=1$ 合并，再用 $\Phi_{41}$ 约化成 40 个坐标。每次乘积都重新约化；不会让后续三个以上因子的未约化次数越过 79。

level-one 形式在所需范围中为
$$
E_4=1+240u^{82}+O(u^{143}),\qquad
E_6=1-504u^{82}+O(u^{143}),
$$
$$
\eta_{\rm Ded}^{12}=u^{41}-12u^{123}+O(u^{143}).
\tag{777.12}
$$
这些是其准确整数 Fourier 公式，不是把原有限域系数直接提升。它们也与已有 R771 模表核对。

全部原椭圆主部补方向仍按 R775 原顺序生成：

- $M_6$ 的普通三积已经有尺度 $82^6$；$E_4M_2$ 方向补乘 $82^4$；$E_6$、$\eta_{\rm Ded}^{12}$ 补乘 $82^6$。
- $M_{12}$ 的普通六积已经有尺度 $82^{12}$；$E_4H^0(4\mathcal L)$、$E_6H^0(3\mathcal L)$、$E_4E_6H^0(\mathcal L)$ 分别补乘 $82^4,82^6,82^{10}$；最后两个 $E_6^2,E_6\eta_{\rm Ded}^{12}$ 补乘 $82^{12}$。

因此最终每个权 $w$ 基行准确等于原基行乘 $82^w$。这个尺度逐行记录，消费者必须除回；它不是新的源模型或目标微分尺度。

每个普通乘积行与每个最终模形式行都独立保存。递归只生成实际被原 recipe 引用的行；缓存命中时按同一配置与 SHA 恢复。所有新基行均与原 R775 在相同有限域点的完整 143 项比较。

## 5. 原 H³ 的 694 阶有理解及全部行尺度

令原 R775 权六基为 $F_1,\ldots,F_{694}$，本阶段整数基为
$\widetilde F_j=82^6F_j$。它们的 Fourier 系数都在 $\mathbf Q(\xi)$，故把 $0\le n\le41$ 的系数分成四十坐标，得到
$$
A_{\rm all}\in\operatorname{Mat}_{1680\times694}(\mathbf Z).
\tag{777.13}
$$
由 (777.3) 它在特征零的列秩为 694。程序在辅助素数 739 上实际选择 694 个原坐标行，并计算所选方阵的非零 determinant。若这个实际有限域步骤未达到 694，本次任务不得宣称成功，必须保留已完成的准确基并处理该实际情况；没有预填某个 determinant 值。

R774 的第 $k$ 个有理坐标行是
$$
[\mathcal H]_k=\rho_k I_k,\qquad 0\le k<14,
\tag{777.14}
$$
其中 $I_k$ 是原 artifact 中的 primitive 整数行，$\rho_k$ 是单独保存的准确有理尺度。坐标顺序为
$1,b,\ldots,b^6,s,sb,\ldots,sb^6$。程序读取前两个 R774 块及同一尺度阶段，核块的尺度 SHA 和偏移；零常数项只添一次。

对所选 694 个原坐标行，置整数右端
$I=(I_0,\ldots,I_{13})$。求
$$
AX=I\quad\text{于 }\mathbf Q,\qquad
A\in\operatorname{Mat}_{694}(\mathbf Z),\quad
X\in\operatorname{Mat}_{694\times14}(\mathbf Q),
\tag{777.15}
$$
并准确验证矩阵恒等式 $AX=I$。使用 python-flint 0.9.0 的 `fmpq_mat.solve(..., algorithm="dixon")`，其结果作为有理矩阵保存；不从模坐标作未经认证的提升。

在**未缩放的原基**中的实际 $L$ 坐标为
$$
\boxed{c_{j,k}=82^6\rho_kX_{j,k}.}
\tag{777.16}
$$
由原 $\mathcal H$ 已在该空间中的理论 membership，及所选原坐标映射的单射，(777.15) 就证明
$$
\mathcal H=\sum_{j=1}^{694}
\left(\sum_{k=0}^{13}c_{j,k}e_k\right)F_j
\tag{777.17}
$$
全局成立。这里 $e_k$ 是 (777.14) 的原 $L/\mathbf Q$ 基。
对某个 $\rho_k=0$ 的行，R774 的 primitive 整数行也为零；该行不会引入额外不定解。

不需要为这个已知同空间的原对象重新生成到 820 阶。该省略使用 (777.3) 和原 membership，不能用于任意未知候选，也不能只凭辅助模 739 的拟合推出 (777.17)。

## 6. 真正 y 恢复的准确接口

本次原 $e=1$ 已由 R774 准确给出。R778 使原 $y$ 的完整关系等价于
$$
[u^n](A-yB)=0,\qquad -1\le n\le141,
\tag{777.18}
$$
每个系数保留全部四十个 $\xi$ 坐标，未知 $A,B$ 的全局基坐标在 $L$ 中。因此本阶段输出的所有权十二基至 $u^{142}$ 已足够。可直接使用 numerator 基，因为原
$D_*=(\eta_{\rm Ded}^{12}/2-sE_6/144)^2$ 在 cusp 是单位。

一个可直接使用 R774 原 $\mathcal H$ 的 Laurent 接口如下。为保留一般归一暂记
$$
\mathcal H=u^e\kappa A_0(u),\quad A_0(0)=1,\qquad
C=-\frac{e^3}{246^3\kappa},\quad c=\frac b{C^2},\quad
y=C\,u^{-e}Z(u),\quad Z(0)=1.
$$
原 $\mathscr D=(1/82)u\,d/du$ 及
$(\mathscr Dy)^3=27(y^2-b)^2\mathcal H$ 给出准确等价式
$$
\boxed{
\left(Z-\frac{uZ'}e\right)^3
=A_0(u)\bigl(Z^2-cu^{2e}\bigr)^2.
}
\tag{777.19}
$$
已知 $Z_0,\ldots,Z_{n-1}$ 后，令 $R_n$ 是暂取 $Z_n=0$ 时左减右的 $u^n$ 系数。真正 $Z_n$ 的系数是
$3(1-n/e)-4=-(e+3n)/e$，所以
$$
Z_n=\frac{eR_n}{e+3n}.
\tag{777.20}
$$
该递推在特征零唯一，无需挑选立方根、另选 $\alpha$ 或 CM 符号。它与原存在的 $f_0(P)=O$ 的局部展开相同。实际 $e=1$ 时，$Z$ 至 142 阶只需要原 $\mathcal H$ 至 143 阶；R774 已有数据足够。

(777.19)–(777.20) 是后继函数阶段的完整规范接口，本阶段核心尚未执行这个数域递推或原 $L$ 核求解。后继一个非零候选必须准确代回 (777.18) 的全部 143 项，或满足 R772 另一套完整全局证书；不能把预期秩 2720、模核或本次权六坐标当作已恢复 $y$。

## 7. 公开计算、断点与大产物

核心为
`scripts/R777_exact_short_K_basis.py`，
包装为
`scripts/R777_public_exact_short_K_basis.py`。
它们只允许在公开仓库的 GitHub Actions 环境执行新算术，固定 python-flint 0.9.0。

每个准确 E1 标签行、实际种子行列式像、普通乘积基行、权六／权十二基行、真实 694 行 minor 与最后有理解都独立保存。恢复时使用同一个完整配置；已完成的行、minor 和有理解不重算。预算到达或异常时保留全部已完成文件与失败凭据，由同一配置继续，不将中断注册成成功。

核心按原 producer 的 manifest 验证每个读取文件。包装额外核真实 run 成功、源提交、artifact ID/ZIP digest、run receipt 和证书，之后才把数据交给核心。原 R771/R774/R775 的数学不会由本阶段再次执行。

大量准确系数只入 artifact。全部阶段 SHA 放在独立
`R777-exact-stages-manifest.json.gz`，小证书只保存该清单的名称、大小、SHA 和计数。完整 artifact manifest 若超过 100 KB，也留在 artifact；Git 保存其小 reference，明确完整 manifest 的 SHA、大小及 artifact 名称。这样所有数据仍可逐项核验，不把数千条基行塞进公开小证书。

最终本阶段成功要求真实准确短基、非零实际 694 阶 minor、完整准确有理等式及正确 (777.16) 全部通过。它不声称已经计算原 $A,B,\beta$ 或高度；后续工作直接接这些准确产物继续原函数恢复。

## 依据

- [R745](../results/R745-certified-original-p41-Hodge-and-adelic-input.md)、[R759](../results/R759-certified-original-integral-period-lattice-and-map-degrees.md)、[R764](../results/R764-certified-original-cusp-images-and-base-translation.md)：原微分、实际第 4 号映射、次数与零平移。
- [R767](../results/R767-original-quotient-low-weight-RR-basis-and-cusp-order-bound.md)、[R772](../results/R772-original-RR-descent-and-exact-function-recovery-certificates.md)：原低权基、算术迹、字段和准确立方归一。
- [R774](../results/R774-certified-original-Hodge-cube-and-cusp-order.md)：真实 $e=1$、原全部 $\mathcal H$ 系数及行尺度。
- [R778](../results/R778-original-cusp-orbit-and-short-exact-recovery.md)：二十 cusp 的实际 Galois 轨道、短注入和 143 项完整函数证书。
- D. Zywina, *Explicit open images for elliptic curves over Q*, [原稿](https://pi.math.cornell.edu/~zywina/papers/ExplicitOpenImage.pdf)，Lemma 4.7 与 Corollary 4.10：原 E1 公式及行列式半线性右作用。
- python-flint 0.9.0 [fmpq_mat 官方文档](https://python-flint.readthedocs.io/en/latest/fmpq_mat.html)：准确 `solve` 与 `numer_denom` 接口。
