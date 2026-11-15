# R827：由实际行列式 Bézout 恒等式认证原整图满射

日期：2026-11-15。状态：**本篇证明新的充分证书及有限执行算法；尚未计算任何新投影行列式或 Bézout 系数，不把该充分条件写成已满足。**

本篇只消费 [原 R827 证明](../results/R827-original-global-modular-surjectivity-and-derivative-termination.md) 的同一真实剩余域、原 $q=4$ 导数列和原完整 cusp 格。它不改动正在续算的 Hermite 消费者，不重算已成原列、导数层、$C$ 坐标换基、模算子或原单位节点。

## 1. 已成原输入与准确矩阵

固定

$$
k=\mathbf F_{1000000753},\qquad n=272,\qquad q=4,\qquad m=n(q+1)=1360.
$$

原 R827 run `43734420663`、source `400edecfeab313d1858cdb72bf18f8452ab9566a` 已在预算结束前完整保存

$$
G(z)=C_\tau(z)^{-1}
 [F_{0,\tau}(z),F_{1,\tau}(z),\ldots,F_{4,\tau}(z)]
 \in M_{272\times1360}(k[z]).
\tag{D1}
$$

列顺序是 $j=272r+c$，先导数阶 $0\le r\le4$、再原 $B$ 乘正规基列号 $0\le c<272$。真实文件为 `R827-tau-layer-rrr-C-column-ccc.json.gz`；共1360条、总 `22969562` B。每条的 `column_coefficients_in_original_C_basis` 是272条按低次到高次排列的完整系数数组，保同一原 configuration、`source_original_layer` 和 `source_complete_C`。

这些列已有真实的首一20次整除及原列乘回证据；新消费者读取原字节、SHA和完成字段，不重新调用 `C_column`。原 $C$ 矩阵是 R820/R827 的稀疏原基

$$
C_\tau e_j=e_j-q_j(z)e_{271}\quad(j<271),\qquad
C_\tau e_{271}=P_\tau(z)e_{271},
\tag{D2}
$$

其中 $P_\tau$ 首一、次数20，所以 $\det C_\tau=P_\tau$。不得换成平方自由多项式、原约化点的部分支撑或另一个整基。

同一来源已有 $\sigma$ 图 $t=0$ 的完整纤维秩272及实际非零 minor `695832206`。它的 `source_C_reduction` 与(D1)一致，并保 $P_\sigma(0)\ne0$。第一图仍缺的是 $G$ 在整个 $k[z]$ 上的满射；原 Hermite 仅完成部分操作，不能冒称为全图证书。

## 2. 少数投影行列式的充分判据

**定理 D.1。** 任取有限组明确保存的常数矩阵

$$
V_i\in M_{1360\times272}(k),\qquad
S_i(z)=G(z)V_i,\qquad d_i(z)=\det S_i(z).
\tag{D3}
$$

若实际得到并准确核实 $a_i(z)\in k[z]$ 满足

$$
\sum_i a_i(z)d_i(z)=1,
\tag{D4}
$$

则 $G:k[z]^{1360}\to k[z]^{272}$ 满射。一个有限表达的真实多项式右逆是

$$
X(z)=\sum_i a_i(z)V_i\operatorname{adj}(S_i(z)),\qquad GX=I_{272}.
\tag{D5}
$$

**证明。** 对任意交换环上的方阵，余子式恒等式给
$S_i\operatorname{adj}(S_i)=d_iI_{272}$，不要求 $d_i$ 非零或为单位。
左乘(D5)得到

$$
GX=\sum_i a_iS_i\operatorname{adj}(S_i)
  =\left(\sum_i a_id_i\right)I_{272}=I_{272}.
$$

全部项都在 $k[z]$，故是整图右逆，而非函数域逆。证毕。

因此机器证书可保 $(G,V_i,d_i,a_i)$ 及(D3)、(D4)的完整准确认证，并以(D5)明确给出右逆；不需要另物化 `1360×272` 右逆或庞大的伴随矩阵。输出必须明确“形式分解的准确右逆”，不能声称已经展开其所有系数。

给定的少数 $V_i$ 可能产生非单位 gcd，即使 $G$ 本身满射；这样的结果只说明所选投影没有通过本充分条件。尤其不能假设块标量投影必然探测全部最大子式。如果遍历全部272列的坐标选择矩阵，则涵盖所有最大子式，单位理想判据是充要的，但本篇不建议或预先启动这个巨大的枚举。

## 3. 与原特征零终止的接缝

保持原 R827 的真实单位分支、整模型来源、原 $B$ 的 $\mathfrak p$-整 lift、原齐次化和完整 cusp target。若(D4)通过，再消费已有的同源 $\sigma$ 无穷远纤维证书，原 R827 推论827.4立即给

$$
\mathscr I_4=\mathscr C_L.
\tag{D6}
$$

理由是(D5)覆盖第一图的全部特殊纤维点；原无穷远秩覆盖其唯一补点；原 proper/Nakayama 引理随后提升到特征零。不重新计算无穷远 jet 或 minor。

这里仍只得到原导数层终止的充分结论。若完整原输入假设保持，原重数界接口可记录 $\lfloor4/3\rfloor=1$；这不等于已恢复原 $D$、$\eta$、主函数、规范高度或全 $p$ 排除。

## 4. 行列式的严格次数界

令原正规基权为

$$
\epsilon=(0,1^{144},2^{127}),\qquad \sum_b\epsilon_b=398,
$$

源列 $j=(r,c)$ 的齐次权为

$$
w_j=5+\epsilon_c+2r.
\tag{D7}
$$

原 source 已认证 $F_{r,\tau}$ 第 $b,c$ 项的次数不超过 $w_j-\epsilon_b$。对(D3)第 $h$ 个输出列，定义

$$
W_h^{(i)}=\max\{w_j:(V_i)_{jh}\ne0\}.
\tag{D8}
$$

若该列没有非零投影系数，则 $d_i=0$，无需节点计算。否则每个 determinant 项使用每一行、每一列恰一次，所以

$$
\deg\det([F_0,\ldots,F_4]V_i)
 \le\sum_{h=0}^{271}W_h^{(i)}-398.
\tag{D9}
$$

又由(D1)、(D2)，

$$
\det([F_0,\ldots,F_4]V_i)=P_\tau\,d_i.
$$

因此，当 $d_i\ne0$ 时，

$$
\boxed{\deg d_i\le D_i:=\sum_hW_h^{(i)}-418.}
\tag{D10}
$$

负的 $D_i$ 强制 $d_i=0$。这利用原准确整除后的完整 $C$ 身份，不是把20个 cusp 当作可无条件删去的数据。新程序可以直接采用已证源次数界；不需要再执行原20次整除或乘回。

所有常数投影的统一界为 $D_i\le272\cdot15-418=3662$。一个计算较便宜的明确投影族是

$$
V(a)=\begin{pmatrix}I_{272}\\aI_{272}\\a^2I_{272}\\a^3I_{272}\\a^4I_{272}\end{pmatrix},
\quad a\in k,\qquad
S(a,z)=\sum_{r=0}^4a^rG_r(z),
\tag{D11}
$$

其中 $G_r$ 是(D1)的第 $r$ 个272列块。$a=0$ 时只取 $G_0$，$D_i=1340$；$a\ne0$ 时 $W_h=13+\epsilon_h$，故 $D_i=3516$。后者只需3517个互异节点，不采用过小的经验次数。

## 5. 由完整节点插值准确得到 determinant

选择 $0,1,\ldots,D_i\in k$，彼此不同，因为 $D_i<1000000753$。对每个节点准确计算

$$
y_{i,j}=\det(S_i(j))\in k,\qquad0\le j\le D_i.
\tag{D12}
$$

节点可以是奇异矩阵，determinant等于零是合法数据，不改选点、不要求逆。次数上界加这些全部值唯一确定真实 $d_i$。这与只在若干点检查满秩不同：这里恢复并认证完整的 determinant 多项式，然后核(D4)。

可用精确 Newton/前向差分插值，无需猜测 Python 是否暴露多项式矩阵类型。令

$$
\Delta^r y_{i,0}=\sum_{j=0}^r(-1)^{r-j}\binom rj y_{i,j}.
$$

因 $r!\in k^\times$，有

$$
d_i(z)=\sum_{r=0}^{D_i}
 \frac{\Delta^r y_{i,0}}{r!}\prod_{h=0}^{r-1}(z-h).
\tag{D13}
$$

实际保存完整系数，核次数不超过 $D_i$，并在已保存全部 $D_i+1$ 个节点代回。节点 determinant 来源绑定到同一个 $G,V_i$；不能在插值后换投影或沿用另一个源的节点。

随后以扩展 Euclid 递增维护

$$
h_j=\gcd(d_0,\ldots,d_j)=\sum_{i\le j}a_{j,i}d_i,
\tag{D14}
$$

每步首一化并完整多项式乘回。遇 $h_j=1$ 时立即记录(D4)而停止新增投影；某个 $d_i=0$ 只保零多项式并继续。全部投影已用完但 gcd 仍非单位，则保存真实 gcd 和未完成标志，不宣称 $G$ 不满射。

## 6. 最小执行契约与续接

初次建议请求明确列出 $a=0,1,-1,2$ 的(D11)投影；它是固定可复核的有限策略，不含成功概率承诺。请求还可列其他明确常数投影，但改变一个投影就必须给独立身份。预算和最多消费多少已预定义投影可以增，已成投影与节点的数学身份不变。

源闭包只需：原实际 run/core/public-input/full-manifest；原 place-and-unit audit、两图 $C$ reduction、原 operator identity/transport index；已有 $\sigma$ infinity certificate；1360条已成 $C$ 列及它们引用的五个原层 index。不得要求不存在的成功 FINAL；原 run 在 Hermite 阶段 BudgetStop，不影响此前同 tag 的完整阶段。来源仍完整保留原 field $B=\lambda b$、原分支0、原 free1186 与原单位条件。

新数学阶段为：

1. 原列来源与实际维数/完整度数检查，记录每条原 SHA，不复制为新标签数学结果。
2. 每个明确投影的实际 $S_i$ 系数矩阵，保由原列线性组合的配方；这一步不重做原 $F_r$ 或 $C$ 整除。
3. 每个节点的完整有限域 determinant，逐节点原子保存；恢复只读已成节点，继续下一节点。
4. 由全部节点得到准确 $d_i$ 及完整插值代回；保存真实 $D_i$ 与实际次数。
5. 完整 Bézout 递推与多项式乘回，成功后按(D5)记录分解右逆及原(D6)接口。

只保存必要的原 source carrier 和上述新完成阶段。预算停止应保全部已成节点/当前投影/当前 gcd；旧 Hermite 的操作记录既不参与新数学，也不需要装入新 carrier。原 Hermite 同核续算可以独立继续，不因本充分消费者存在而取消。

工程可直接使用 `python-flint==0.9.0` 已文档化的 `nmod_mat.det()`，矩阵系数 Horner 求值；`nmod_poly` 的加乘、`divmod` 和 `xgcd` 可完成(D13)、(D14)。原生 FLINT 也提供 `nmod_poly_mat_det_interpolate`，采用次数界、有限域 determinant 和完整插值；本方案不依赖未经确认的 Python poly-matrix 封装或临时 ABI。

主文档：[python-flint 0.9.0 nmod_mat](https://python-flint.readthedocs.io/en/latest/nmod_mat.html)、[nmod_poly](https://python-flint.readthedocs.io/en/latest/nmod_poly.html)、[FLINT polynomial-matrix determinant](https://flintlib.org/doc/nmod_poly_mat/nmod_poly_mat_det.html)。这些只支撑软件接口；数学证明已在上述各节给全。

## 7. 当前准确来源登记与未算内容

原 R827 artifact `14180474398`，ZIP `3646481834` B，平台 SHA按实际请求绑定；原 full manifest `19902271` B，SHA256 `2609de217bf1da048f7987ae7de09df38ac24fb63e82d45add1e7c6b9cdbea7e`。必要小源：

- 原 place/unit audit：`4261` B，SHA256 `7f4d511a9871d31d38565703211d7f14636a195b9fa2db48818996afb084e883`。
- 两图原 $C$ reduction：`79991` B，SHA256 `4b5d3828f164a2b8db43ee4227938b03a7d78acbe26aaff39b5dfb2b2fce09fd`。
- 原 operator identity/transport index：`2479` B，SHA256 `8aebc342bd263a00f306de6b2b6fc1775a7a246cf06622152e7d5c9edd5410a6`。
- 原无穷远证书的实际秩272/minor695832206已读；完整 SHA 由同一原 manifest 直接核，不按摘要补写。

截至本稿，没有新的 $d_i$、gcd、Bézout 或(D6)结果。源码、参数、纸面证明和简明运行/SHA可登记Git；原列、节点、系数和机器回执只在一日 active artifact/carrier 中保全续传。
