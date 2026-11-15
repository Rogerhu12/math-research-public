# R133：保存的正 collar 组件与十二个高频 coercivity 门的实际结论

状态：公开 scientific child 已真实完成，16 个完整性门与 12 个 coercivity 候选全部通过。原 workflow 因最后出版包装超过字节门而为 failure；本文完整保留该历史，只恢复已打印且 SHA 核实的结果，不重新运行数学。

## 1. 唯一运行、原身份与完整恢复

本篇消费 [LC 合同](R133-supplement-saved-positive-collar-component-bounds-and-high-frequency-coercivity.md) 的同一真实对象。公开 [run 43731225532/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43731225532)，job `132863865114`，由 head `003e6ee56848a4b6a948af56b0e3ac4f768d467f` 的 push 自动启动；没有第二次 dispatch。

- Run 创建于 `2026-11-15T15:40:51Z`；job 为 `15:40:54Z` 至 `15:41:36Z`。
- Scientific child 为 `15:41:30.495107+00:00` 至 `15:41:32.495758+00:00`，真实 return code 为 0。
- 新标量科学段记录 `0.7718212529999988` 秒，320 bit 有向算术。
- SCI SHA256 为 `02fc50c45ed2610b94619d9db60ee2f74dc3a1643ce2f398c8eb25505926f7ea`；worker 为 `02bc473c3e87105fd8484e603cffa18bc9f160b4becf3501323f7b3e24b0aeeb`。
- Manifest 为 `3a172b9e41587c50bd8f3112b3ef98b0c33a736a75b1204e2d627ef82767766c`；16 个输入身份均通过。
- 旧 native 精确 6,223,338 B，SHA256 为 `ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d`。四个旧 parts 逐字恢复，全 4650 行覆盖门保留。
- 新限制准确取 $I=[17/20,19/20]$，cut 为 $c=9/10$，140 个原闭行，真实总 $dr$ measure 为 $1/10$。所有这些行的 provenance 均为原 `same_intrinsic_cap_v2`。

原 worker 在首次最终 Git publication 前打印的 `PREPUBLICATION_STATUS` 为：

$$
 \mathrm{child}=0,\qquad \mathrm{complete}=\mathrm{true},\qquad
 \mathrm{gates}=16/16 .
 \tag{LCA.1}
$$

原完整 science 的 pretty JSON 为 74,725 B，SHA256
`903a537a0454464e8c30ff57034b2811d1c43ad47a18979f5a7d8403c888b981`。
原同时打包 science 与 report 的 payload 为 66,478 B，超过 59,000 B 限制；
其 SHA256 为
`0c454a9c0d0b5934da65aff6523a67a79f17d4ff0bec4c8c854f4a2a1cf89076`。
worker 因此记录 `publication_failure`，没有发布新的原始大对象。

但其最后保留分支把完整 final process 和完整 science 打印到日志。恢复时只剥每行 GitHub 时间戳，得到的原 science 字节数与 SHA 均准确匹配；再按冻结 worker 的纯格式函数重建 report 和完整 payload，也准确匹配上面的 66,478 B 与 SHA。没有重新评价任何球、积分、系数或候选。

保存的 [完整 science](../notes/saved_positive_collar_components_ci/run-43731225532-1-saved-positive-collar-components/actual-saved-positive-collar-components.json) 只去掉 JSON 字符串外空白，保留全部字段、数字 token、有向球、原行极值身份、六张表和十二个 verdict：

$$
 \mathrm{bytes}=55770,\qquad
 \mathrm{SHA256}=
 \texttt{44b4da07b50dcca9be7671b8cb59b227999e76871237c25a1bc0aec4bc02492c}.
 \tag{LCA.2}
$$

重新按两空格缩进即可逐字恢复原 74,725 B / SHA。完整 [final process](../notes/saved_positive_collar_components_ci/run-43731225532-1-saved-positive-collar-components/process.json) 保留真实 child、原 README pull、全部输入 SHA、容量测量和 publication failure；[原 actual report](../notes/saved_positive_collar_components_ci/run-43731225532-1-saved-positive-collar-components/actual-result.md) 与 [恢复记录](../notes/saved_positive_collar_components_ci/run-43731225532-1-saved-positive-collar-components/recovery.json) 单独保存。先前 Git 中 11,141 B 的 process 只是数学开始前 checkpoint，没有冒充 final process。

## 2. 数值结论的真实域

保持 LC.1--14 的全部量词。$Q_0$ 为原 degree32 centre 加完整连续修补，$Q_\delta=Q_0+\delta Z_{\rm can}$，$|\delta|\le10^{-10}$；$Z_{\rm can}$ 为完整 canonical degree96 方向，包含 piecewise constant 连续修补，不是径向 mean-completed trial。考虑在整 $I$ 上同一个真实、连续、两侧 $H^1$ 解 $Q$，其 ordinary residual 为零，且

$$
 \|Q-Q_\delta\|_{C^0(I\times\mathbb T)}\le\rho,
 \qquad
 \rho\in\{10^{-4},2^{-20},2^{-24},2^{-28},2^{-32},2^{-36}\}.
 \tag{LCA.3}
$$

这里沿用 LC 的 pair 范数和 normalized moving circle。表中的 $a_-$ 是实际 principal speed 的下界，不能替代 intrinsic 径向坐标 $a$。所有未知量仍是同一状态；右帽已付的单侧 $C^0$ 门不自动支付左半窗或整个 (LCA.3)。

对非零 residual 的近似态，LC.10 所需额外 mean-residual logarithmic-speed 项和真实高源仍必须另付；本次十二候选不授予该额外项。

## 3. 实际完整组件

直接由保存的原字段、原 mean、原完整 signed $S$ mean 及 LC 的三种修补，得到以下向外简写。各原球与取得极值的完整闭行都在 science 中；这些小数只是把该结果向外放宽。

| 量 | 已成全窗上界 |
|---|---:|
| $\sup_I\|P\|$ | $1.714577710$ |
| $M_0$ | $2.097108316$ |
| $M_1$ | $0.210989757$ |
| $N_0$ | $0.051824436$ |
| $M_{\rm av}$ | $2.076924714$ |
| $b_+$ | $1.311133100$ |
| $\alpha_+$ | $5.714332467$ |
| $g_+$ | $2.015429469$ |
| 原 saved drift | $0.047091050$ |
| 原 saved drift 第一角导 | $0.190048323$ |
| $A_{\rm mix}$ | $1.114172417$ |
| $A_{\rm ref,\delta}^{>J}$，$J=96,288$ | $6.660216802\,10^{-8}$ |
| $C_{S,96}$ | $19.197135511$ |
| $C_{S,288}$ | $55.363061700$ |

原 $V_{\ne0}$ 是直接保存的完整 nonmean，未用两个独立 norm 相减。$M_{\rm av}$ 的 even mean 始终保留。$P$ 的两个分量分别使用正确 $K$ 球端点，没有再乘物理 $\alpha$。

最宽 $\rho=10^{-4}$ 候选已得到

$$
 \begin{aligned}
 m_-&>2.896910824,& a_-&>3.669992340,\\
 L&<9.476043153,& d_+&<0.047740670,& A_H&<21.851224633.
 \end{aligned}\tag{LCA.4}
$$

其余五个候选各自有完整有向球。两个 intrinsic logarithmic derivative 输入仍逐字来自既成 D execution
`6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071`：
$L_G<2.225717176$、$L_K<9.447222797$。
没有再次恢复或计算 D 的 7721 行。

## 4. 全部十二个真实频率门

对 $J=96,288$，真实第一高频分别为 $n_J=388,1156$。记

$$
 \tau_J=\frac{L}{a_-n_J},\quad
 c^\#_{p,J}=\frac1{a_-\sqrt{1-\tau_J}},\quad
 t_J=\frac{c^\#_{p,J}A_H}{n_J}.
 \tag{LCA.5}
$$

每个候选先检验实际负 mean gap，再分别检验 $\tau_J<1$ 与 $t_J<1$。
所有十二个候选的这三个前提均实际通过；不存在被省略的失败候选。
$\bar c_{p,J},\bar c_{r,J}$ 为 LC.19 的吸收后两常数，
$V_J=p_c\sqrt{\kappa_J\bar c_{p,J}\bar c_{r,J}}$ 为 LC.21 的 half-trace source gain。
下表每个数均为严格上界。

| $\rho$ | $J$ | $\tau_J$ | $t_J$ | $\bar c_{p,J}$ | $\bar c_{r,J}$ | $V_J$ |
|---|---:|---:|---:|---:|---:|---:|
| $10^{-4}$ | 96 | .006654726 | .015396741 | .277666482 | 1.028893491 | .916441681 |
| $10^{-4}$ | 288 | .002233593 | .005156303 | .274198801 | 1.018273462 | .905987576 |
| $2^{-20}$ | 96 | .006653348 | .015395359 | .277656407 | 1.028712936 | .916344641 |
| $2^{-20}$ | 288 | .002233131 | .005155842 | .274189236 | 1.018096122 | .905892880 |
| $2^{-24}$ | 96 | .006653335 | .015395346 | .277656316 | 1.028711306 | .916343765 |
| $2^{-24}$ | 288 | .002233127 | .005155838 | .274189149 | 1.018094522 | .905892025 |
| $2^{-28}$ | 96 | .006653335 | .015395346 | .277656310 | 1.028711204 | .916343710 |
| $2^{-28}$ | 288 | .002233127 | .005155838 | .274189144 | 1.018094422 | .905891972 |
| $2^{-32}$ | 96 | .006653335 | .015395346 | .277656310 | 1.028711198 | .916343707 |
| $2^{-32}$ | 288 | .002233127 | .005155838 | .274189143 | 1.018094415 | .905891968 |
| $2^{-36}$ | 96 | .006653335 | .015395346 | .277656310 | 1.028711198 | .916343707 |
| $2^{-36}$ | 288 | .002233127 | .005155838 | .274189143 | 1.018094415 | .905891968 |

## 5. 完整未知列没有变成已知量

在同一宽窗置

$$
 z=P(Q-Q_\delta),\qquad
 Z_{L,J}=\|\Pi_Jz\|_2,\quad
 Z_{S,J}=\|(\Pi_J-\Pi_{J-64})z\|_2,\quad
 Z_{H,J}=\|H_Jz\|_2 .
 \tag{LCA.6}
$$

范数为 ordinary $L^2(dr\,d\phi)$。$Z_{L,J}$ 包含 even mean；
两个 shell 分别为 quarter labels $33,\ldots,96$ 与 $225,\ldots,288$。
实际表给出

$$
 \|H_J(Q-Q_\delta)(c)\|_{H^{1/2}_\phi}
 \le V_JF_J+
       (V_JC_{S,J})Z_{S,J}+
       (V_JC_{L,J})Z_{L,J}+
       20V_JZ_{H,J}.
 \tag{LCA.7}
$$

各项真实已成 scalar 系数均保存，没有把 shell 或 high-body 量设为零。
例如最小候选 $\rho=2^{-36}$ 可直接放宽为

$$
 \begin{aligned}
 \|H_{96}(Q-Q_\delta)(c)\|_{H^{1/2}}
 &\le.916343707F_{96}
  +17.591174306Z_{S,96}
  +4.071553329\,10^{-6}Z_{L,96}
  +18.326874128Z_{H,96},\\
 \|H_{288}(Q-Q_\delta)(c)\|_{H^{1/2}}
 &\le50.152952902Z_{S,288}
  +1.195433269\,10^{-5}Z_{L,288}
  +18.117839355Z_{H,288}.
 \end{aligned}\tag{LCA.8}
$$

第二行使用同一 true residual-zero 状态的 $F_{288}=0$；
它来自完整 degree288 canonical residual，而不是凭 reference 本身 degree96。
$F_{96}$ 仍为既成 NR/WC 的同窗完整高源，本次未重积分。
原 raw mean 的 MC 费用在 full equation 中保留，只在正确高投影中准确消去。

为使低输入费用的六个候选完整可比，给出 $V_JC_{L,J}$ 的向外上界：

| $\rho$ | $J=96$ | $J=288$ |
|---|---:|---:|
| $10^{-4}$ | .328831148 | .972908939 |
| $2^{-20}$ | .003139587416 | .009288982916 |
| $2^{-24}$ | .000199996228 | .000591635288 |
| $2^{-28}$ | .00001627199012 | .000048051679122 |
| $2^{-32}$ | .000004789226078 | .00001407770600 |
| $2^{-36}$ | .000004071553329 | .00001195433269 |

这里的显著缩小来自实际 saved nonmean 组件、实际 drift 和两个真实频率吸收；
没有改变未知实际 $Z_{L,J},Z_{S,J},Z_{H,J}$，也没有给出原 finite193 receiver 的新输出 Gram。

## 6. 已付范围与仍未付的输入

本次 16 个完整性门支付原身份、覆盖、保存字段、已成 D 输入、
canonical 修补和候选记录的完整性；12 个候选支付声明域内的实际 mean/两能量门。
二者不能混称为“28 个同类门”。

全部 source、mean 和 cutoff 的职责保持：

1. 三角 cutoff 的真实 $20Z_{H,J}$ 列不可因 high-input 吸收而删除。
2. 已知 Wiener primitive 的 $1/4$ 与未知 $C^0$ sawtooth 的 $\pi/8$ 分别收费。
3. 有限 rank mean 输出只在最终 $H_J$ 后消失；低输入 mean 和实际 mean 条件没有删除。
4. 实际物理乘子 $P$ 在 (LCA.7) 返回 raw moving trace 时只付一次。
5. 若要继续用 $H^{8193}$ 插值，必须是同一个真实状态且另在窄 MA 五例的已付域内。本表不扩大 MA 的区间或 $\rho$。
6. 目前没有新增真实 unknown cut、shell、high body 或 receiver 的数值界；没有证明低曲率 entry、自映射、core 存在或全 matching。

完整逐行新审计为 3,533,437 B，
SHA256 `135dbe6f2bcbfd1146aed48fca201f514c2bdec41ce8cd40a42acf6757f949fb`；
只在原 runner 临时目录生成，没有持久保存。
旧 target/Fourier/trial/convolution/residual/repair/mean-flow/Green 调用均为 0，
source integral 新计算为 false。此次恢复也没有重复任何这些工作。
