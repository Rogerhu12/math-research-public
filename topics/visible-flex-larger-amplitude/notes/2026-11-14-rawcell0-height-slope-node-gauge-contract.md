# RawCell0 的高度斜率节点坐标：实际41输入与原边界合同

本条把 [R269](../results/R269-native-zero-reference-height-slope-gauge.md) 的节点变换绑定到 actual41 已保存对象。只使用源码、原件和代数；没有生成 G 数值、变换矩阵或实施求解。本文件在终端失联后从已完成说明重建，具有新的字节身份，**不冒作此前本地 15164 字节、SHA e658c7d580ea44c60771a0b1b7a2136c92cbb3a734d172926ff00a4633ad7252 的原文件**。以下实际来源、公式和范围保留。

## 1. 固定系统及映射

actual41 是公开 run `43622149326`，source `0beffe5a963015a4063a8c53d4a92fec32205005`。其 `result.json` SHA 为 `6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf`；summary 为 `ab20cc260b8a0a1e6642aa26c70b11575dee9a9245ac467482d8095f410e9594`；layout 为 `5f2e7ea49915dfca676277c81ef4e5463eab72bdcb1882aba437630a69d59ef4`。原576父场为 actual28 `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7`。

固定 M=112、spacing=2、K=224，所有非零模式 $m_j=2(j+1)$ 均保留。原节点顺序是全部 Q 后全部 Pi，不是交错模式顺序。完整226状态跨每一步持续，原224形状矩阵不包含两个独立 mean 积分状态；此事实不许可省去原最终 mean/readout。

旧 rawCell0 的72段共868步，旧 stage11、28、31、63 各13步，其余12步。扩展系统深度 $D=1372=868+504$，节点1373，旧577节点通过 `oldToNew` 保留。源绑定器为 `exact_20261114_rawcell0_step_system.py`，SHA `fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81`。

设旧段 n 起点 $t_n=\mathrm{oldToNew}[n]$、原步数 $L_n$。流的第 k 步对应

$$
i_{\rm in}=t_n+L_n-k,\qquad
i_{\rm out}=t_n+L_n-1-k,\qquad 0\le k<L_n.
$$

原最后一 RK 步对应新 shooting 段 $t_n$，此处才应用原出口 port。完整新系统仍为

$$
J_i\delta_{i+1}-\delta_i+r_i=0.
$$

其 J/r 是868个实际短块加504个原块；不是同时施加旧72个长 J。

## 2. 原 μ、port 与实际几何

原 `78718-tail-fourier-root-momentum.mjs`（SHA `cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88`）定义

$$
\Pi=\frac{\varepsilon r^4(\omega_\theta-1)}{\sqrt{12}\mu},
\qquad w=\exp(\mathrm{profile.logw}).
$$

实际 live parameters 的 orientation=1、modes=112、spacing=2。每段 μ 必须来自其原 engine/cell 元数据，不得用一个全局 μ 替代。

原 `78718-tail-tangent-core.mjs`（SHA `ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3`）的 cellFlow 出口为

$$
Q_{\rm stored}=Q_{\rm engine},\qquad
\Pi_{\rm stored}=\Pi_{\rm engine}/\rho_n,
\qquad \rho_n=\mathrm{cell.portRatio}.
$$

已保存 J 的 Pi 行也已除同一 port；cutJets 先把 node0 的 Pi 乘回 $\rho_0$ 再交原 engine。因此

$$
G_{\rm stored}=G_{\rm eng}\operatorname{diag}(I,\rho_nI).
$$

G 的 Pi 列应乘 port，不是除 port。实数上可称有效 $\mu_{\rm node}=\rho_n\mu_n$，实现仍应保 `source_mu` 与 `pi_to_engine_factor` 两份原来源，避免提前舍入出另一个无来源 μ。

实际 rawCell0 μ 为 `1.0048110027994864e-11`，cut port 为 `6.727171322029716`；旧 stage72 的 rawCell1 μ 已是 `1.4936604922027106e-12`。数学比例关系不许可忽略它们的实际浮点身份。

G 使用 `root.g.r`，不使用同记录的历史 `oldR`。w 使用已保存 `root.g.w`，不重新 exp(logw) 或 sqrt(w2)。源码分别计算 w 和 w2，不能假定两条浮点路径逐位相等。

实际 cut r 为 `0.30000000000000004`，f64le `343333333333d33f`；w 为 `0.08000000000000027`，f64le `8e14ae47e17ab43f`。不得用方便的十进制 .3/.08 覆盖。原 H、已形成 target Q、cut residual 均保原字节，不重新归一化。

## 3. 每节点唯一且有来源的 G

采用最小局部方案：新节点0至868使用 G，新节点869至1372取确切单位阵。全部504原 J 仍复用，不新增后段 profile/root/RHS 求值。旧 stage72 位于新 stage868，是左 G、右 I 的完整接口块，不能漏掉它的左乘。far 节点 G=I。

`fields[n][k,f]` 表示第 n 段 field packet 中 global_step=k、field_index=f。每份原 packet 的压缩和解压 SHA 先绑定；window identity 给 μ 及原 port。

| 节点 | 唯一 anchor | Pi 坐标约定 |
|---|---|---|
| cut0 | stage0 最后步 field3 的几何 | μ0；Pi-to-engine factor=原 port0 |
| $t_n+L_n-k$, $0\le k<L_n$, $0\le n<72$ | 同 n、k 的 field0 | 该段 μ；factor=1 |
| 869至1372 | identity 类型 | 不伪造 r/w/μ |

第二行一次覆盖节点1至868，包括全部插入点。旧共享 node n（1至72）统一取外侧 stage n−1 的输入端。禁止在相邻两段中给同一节点分配两套 G。

这与原 core 的 nodeR 约定一致：node0 取最外 profile 端点，其余旧节点取外侧段输入。纯字节核验中，868个首 field0 的完整226状态 SHA 均等于对应 `full_states[k]` chunk。cut 的 field3 只用几何；其临时 RK 状态不是完成步后的状态，不能把状态身份混同。原 geometry(profile,x) 与状态无关，故读取该几何不需重解根。

唯一 anchor 有实际必要：相邻 RK 端点的 r/w 在6个内部节点不逐位相等（stage12/k10、13/k7、13/k10、44/k7、44/k10、45/k7）；旧共享 node16、24、56 两侧 w 也不同。这里仅比较原 bits，没有新算差范数。不能平均，更不能两边各取一个值后仍称同一节点变量。

以下选择器只搬原记录和整数索引，不形成 G：

```python
def select_node_gauge_records(layout, reports, windows, packets):
    D = layout['newDepth']
    offsets = layout['oldToNew']
    plan = [None] * (D + 1)

    def anchor(n, k, field_index, node, factor, completed_node):
        rows = [row for row in packets[n]['fields']
                if row['global_step'] == k
                and row['field_index'] == field_index]
        assert len(rows) == 1 and plan[node] is None
        row = rows[0]
        plan[node] = dict(
            kind='R269-reference-node-gauge', node=node,
            original_stage=n, global_step=k, field_index=field_index,
            field_packet=reports[n]['field_observations'],
            window_identity=reports[n]['identity'],
            source_mu=windows[n]['mu'],
            pi_to_engine_factor=factor,
            r=row['geometry_number_fields']['r'],
            w=row['geometry_number_fields']['w'],
            field_state_sha256=row['state_float64le_sha256'],
            field_state_is_completed_node=completed_node,
            completed_full_state_array=(
                reports[n]['arrays']['full_states']
                if completed_node else None),
            completed_full_state_row=k if completed_node else None)

    one = dict(value=1, float64le_hex='000000000000f03f',
               classification='finite')
    for n in range(72):
        L = reports[n]['step_count']
        assert offsets[n+1] - offsets[n] == L
        for k in range(L):
            anchor(n, k, 0, offsets[n] + L - k, one, True)
    anchor(0, reports[0]['step_count'] - 1, 3, 0,
           reports[0]['original_port_ratio'], False)
    for node in range(offsets[72] + 1, D + 1):
        assert plan[node] is None
        plan[node] = dict(kind='exact-identity-node-gauge', node=node)
    assert all(record is not None for record in plan)
    return plan
```

后继保存 node-plan SHA、每个输入 scalar 的原 f64le bits、生成源码身份及实际 G 系数 dtype/shape/raw SHA。不能靠短十进制重建。

## 4. 完整二元块与有限系数定义

对非 identity 节点，定义

$$
\alpha_n=r_n^4,\qquad
\beta_{nj}=m_j^2r_n^3,\qquad
\eta_n=\frac{\varepsilon\sqrt{12}\mu_n\rho_*}{r_n^4w_n},
\qquad
G_{nj}=\begin{pmatrix}\alpha_n&0\\\beta_{nj}&\eta_n\end{pmatrix}.
$$

恢复式为

$$
\delta Q_j=\xi_{u,j}/\alpha_n,\qquad
\delta\Pi_j=(\xi_{k,j}-\beta_{nj}\delta Q_j)/\eta_n.
$$

identity 节点明确 $\alpha=\eta=1,\beta_j=0$，不虚构几何。完整块仍放在原 Q-all/Pi-all 顺序。此式是 R269 的 $u=r^4q$、$k=r^3(m^2q+bp)$，包含 stored-Pi port。k 只在所述零参考连续系统上等于高度斜率；对实际非零场，它是可逆线性坐标名称，不能代替原物理 jets。

形成时固定精度与括号次序并保存实际系数。例如先形成 r3、r4，再形成所有 m*m*r3 以及 `(((orientation*sqrt12)*mu)*port)/(r4*w)`。这只是明确 recipe 的例子，不预断普通 binary64 足够；若用 longdouble，必须记录其实际 dtype/位宽及最终落盘字节，不能冒作 exact 或另一种位宽。

实际保存 alpha/eta 必须有限非零；否则是坐标表示失败，不能删模、改 H 或冒称原科学门失败。把形成后的有限系数视为确切 dyadic 实数时，其数学逆由这些实际系数定义。它们不自动等于含精确平方根的参考 G。R269 对任意明确可逆 G 的有限矩阵命题仍成立；计算的矩阵形成和恢复误差另记。

## 5. 全耦合变换与原边界

对所有完整 stage，使用

$$
\widetilde J_i=G_iJ_iG_{i+1}^{-1},\qquad
\widetilde r_i=G_ir_i,\qquad
\widetilde J_i\xi_{i+1}-\xi_i+\widetilde r_i=0.
$$

J 已含原出口 port，上式不再追加 port。保全部112×112模间耦合。实际非零 J 不用零参考逐模 ODE 替代。

输出模 i、输入模 j 的原 QQ、QPi、PiQ、PiPi 条目记为 A、B、C、D，右节点系数加号。完整变换是

$$
\begin{aligned}
\widetilde A_{ij}
 &=\frac{\alpha}{\alpha_+}
       \left(A_{ij}-B_{ij}\frac{\beta_{+j}}{\eta_+}\right),\\
\widetilde B_{ij}&=\frac{\alpha B_{ij}}{\eta_+},\\
\widetilde C_{ij}
 &=\frac{\beta_iA_{ij}+\eta C_{ij}
       -(\beta_iB_{ij}+\eta D_{ij})\beta_{+j}/\eta_+}{\alpha_+},\\
\widetilde D_{ij}&=\frac{\beta_iB_{ij}+\eta D_{ij}}{\eta_+}.
\end{aligned}
$$

这是实数代数合同，不保证浮点相减无损。实际形成精度、顺序、单舍入和损失须明确。当前节点项保持确切 −I，不重新乘一个舍入的 −G*inverse(G)。节点邻接、方程数和 cut→stage→far 行序保持，原 kl112/ku335 可保留。

原 cut 已保存 $r_c=Q_0-\mathrm{target}$，不额外缩放此行时：

$$
\xi_{u,0}/\alpha_0+r_c=0.
$$

不要直接把右端换成 physical H。原 target 是实际舍入 H/r^4，再乘 alpha 不保证恢复相同 H 字节；三份原 identity 都保留。

原 far 行为 $\delta\Pi_D-\Gamma_D\delta Q_D+r_f=0$。当前 $G_D=I$，逐字保全全部112个原 far graph 系数。若未来明确扩展到 far，完整行必须变成

$$
\frac{\xi_{k,D}}{\eta_D}
-\frac{\Gamma_{D,j}+\beta_{Dj}/\eta_D}{\alpha_D}\xi_{u,D}
+r_{f,j}=0,
$$

不能换成新参考 graph。当前合同不需要此扩展。

## 6. 原 sigma、全行 exact 读回及原试步

全部旧 sigma 原字节保留，插入节点仍取其旧父段 sigma，不以 G 生成新 scaleFor/gains。任何额外可逆均衡只作为求解表示，另作身份账。

若精确新 stage 缺陷为 $(\widetilde e_u,\widetilde e_k)$，则

$$
e_Q=\widetilde e_u/\alpha_i,\qquad
e_\Pi=(\widetilde e_k-\beta_i e_Q)/\eta_i.
$$

原范数是全部 cut/stage/far 行的 $\max|e|/\sigma$。G 含剪切，不能以新坐标范数或仅对角倍率代替原范数。

实际 rounded xi 经三角式恢复 rounded delta 后，保存完整 delta 字节，再用既有动态 all-rows exact dyadic reader，在**原坐标的1372块 J/r、原 cut/far、原 sigma**上逐行读回。它报告矩阵形成、求解及恢复误差的合成后果。舍入后的新 J 不能自动视为精确 GJG-inverse；若要分解形成/恢复误差，可独立记录，不把该诊断另设科学门。[R266](../results/R266-native-block-Newton-defect-and-original-scaled-descent.md) 的浮点数组、数学导数和非线性余项区别不变。

新输出绑定：node-plan SHA、实际 G 系数 SHA、新矩阵身份、原1372系统 binding、完整恢复 delta、按 oldToNew 的577-node restriction，以及各轮原 exact residual。不得把该 restriction 冒作旧576 correction；旧长 J 缺陷继续仅作诊断。

后续 nonlinear trial 回到完整原577节点、原 H、far、原10试步和原 evaluate，不能在 u/k 坐标另写一个近似 acceptance。本合同不把 G 放进 RK 各级，不重积分、不增删步、不改 profile/μ/根容差/N2048/分支。连续换坐标后重新 RK 是另一个有限算法，仍须按 R269 §6 区别。没有依据本合同预先证明条件数改善、native 接受或课题完成。
