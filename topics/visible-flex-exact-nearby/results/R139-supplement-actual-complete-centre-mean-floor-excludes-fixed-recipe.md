# R139 补篇：完整中心均值下界实际排除固定小范数配方

2026-11-20，`visible-exact-astra-ac637-20261120`。

**已证明：原固定 W2C 小中心比较配方不能通过。** 同一完整 signed centre 的均值原子给出 $K^2>6409$，故 $K>80$；该配方的必要条件是 $K+\epsilon<1/128$。这是配方的严格排除，不是真实算子奇异、原边值问题无解或本课题完成的证明。

## 1. 唯一实际运行及完整输入

公开 [44727185157/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44727185157) 成功。workflow 事件提交为 `5791d0bf6d239296e044a050569d53e1e39f7c02`，实际科学 checkout 为 `fbbae101510e645b10c5ec2d71000f4e565150ee`。

完整 [75 项输入清单](../notes/2026-11-20-centre-mean-floor-inputs.json) 为 74663 B，SHA256 `e08f68211772528adac26363757f43998328f3d2a7f9dbbcea5f59f4db86a7af`。owner 为 `fourfold_codazzi_centre_mean_floor_diagnostic.py`，33188 B / SHA256 `794cc3d9b7fada56b5112421bbaeb9ceb74144bfdbb58e317ad17ed34f4c59b0`；只消费原完整中心的 signed mean entry，未运行原 L、旧 mean-atom 或 endpoint 成功目标。

| 完整输出 | 字节数 | SHA256 |
|---|---:|---|
| [actual](../notes/centre_mean_floor_ci/run-44727185157-1/actual-scientific-conclusion.json) | 90908 | `7eedd9385a638b1cfe657c07141fd7ea275755186f497ac77c290ee595c1c042` |
| [execution](../notes/centre_mean_floor_ci/run-44727185157-1/execution.json) | 56440 | `0aff9f66338ed108314cd6ed2ab2dc1a2632ab79ded5f2ef8fc6418a54417eb0` |
| [report](../notes/centre_mean_floor_ci/run-44727185157-1/report.md) | 527 | `74602c24869add8ecd85fc5e7f9f1941fd2c87d14301e352b282b35a63499080` |

root 逐项核75份完整当前输入及 worker 的 bytes/SHA/Git blob，actual 与 execution 的75项回执完全相等；25项 AST、七个原模块及 owner/proof 身份一致，27门全部通过。原21件恢复、153个 parent、155个比较 panel、4650条旧闭行和4801个交段完整保留。原29球、candidate/repair、全部原 scope、参考身份、两个 optical 记录和全部旧成功/失败对象与已核原 L 结果逐对象相同。

唯一科学 child 返回0，wall `88.13578711900001` 秒，数学部分 `78.91366354299998` 秒；4次实际 pull 后两 README 差异均为空。当前目标与 failure 均 null。0旧成功目标重算，0新数组、artifacts 或 Releases。

## 2. 一个完整下界及其数学对象

[解析补篇](R139-supplement-complete-joint-centre-mean-atom-lower-bound.md)已证明：degree32的完整中心作用于纯 even mean 后角输出至多64，因此 $B_{HL}^c e_m=0$，整个 $C F B$ 在该输入上严格为零。原 $P_f$ 保留 root-mean atom 不变，且此原子的准确核为 $-a_{00}(r)/q(r)$。于是对原 ordinary radial $L^2$ body 输入，

$$
K^2\ge\|P_fH_c\iota_B\|^2
\ge J:=\int_I|a_{00}(r)/q(r)|^2\,dr.
$$

这里是完整 signed centre 的下界，不是以某个保守上界当真实算子下界。连续中心另有同一 $J$ 下界，但不需要、也不宣称 $K\ge\|H_c\|$。同 actual-eta hybrid、原 moving-phi 角、独立 mean 和原 $S$ 全部保留。

全部155个 panel 完成后，唯一新保存记录 `complete_joint_centre_mean_atom_squared_norm_lower` 为：

```text
[6409.59093747500317968874325858840528173828638122141989445756634629317488577 +/- 3.16e-72]
```

每个 panel 消费 `context.centre_matrix(((1,0),),((1,0),),whole_panel_box)`；以完整 signed 球离零距离的有向下界、真实长度下界和原 $q$ 上界，累加

$$
J_{\rm lower}=\sum_i
(h_i)_{\rm lower}\,
\frac{\operatorname{dist}(0,(a_{00})_i)_{\rm lower}^2}
     {(q_i)_{\rm upper}^2}.
$$

实际146个 panel 有严格正距离，另外9个贡献0；没有删去这些 panel，也没有用中点代替完整系数球。唯一结果先完整保存，再读回其下端点作比较。

## 3. 排除门及后续范围

保存球的下端点严格大于6409，因而大于 $80^2=6400$，更大于原准确阈值 $1/16384$。实际 `fixed_recipe_rejection_proved=true`，结果为 `fixed_small_centre_recipe_excluded`。

[原必要预算](R139-necessary-budget-for-fixed-W2C-comparison.md)已经给出，对此固定配方与 $h=K+\epsilon\ge K$，

$$
G\ge\frac{109}{120}+\frac{963}{80}h.
$$

仅用原 $K\ge1/128$ 阈值已得 $G\ge30793/30720>1$；本次更强的 $K>80$ 还直接给 $G>115669/120>1$。这些是对既定正比较公式的下界；并不求值原五个完整 graph 或宣称真实残差有同一下界。

原 L 三条 [44724797559/1](R139-supplement-actual-complete-low-family-budget.md) 完整原球在本次只读保留，原合同仍是3/50已算；此次独立一条下界不计入那50条。其余47条未算，且不再为这个已排除的固定配方继续计算。所有旧失败、独立 atom 三条和 balanced endpoint 成功保持原状态并冻结。

实际 `parent_candidate_complete=false`、`finite_gate=null`、`conditional_finite_inverse=null`、`actual_operator_singularity_proved=false`。后续改由 R141/R137 直接中心边值逆及几何能量路线推进；全部 CFB、真实系数差、finite投影/lift/normalizer、七 ports、两 RHS、物理96列、Theta/nu/两 mean、负侧、非线性和单一闭面匹配继续保留。最终精确可见族尚未构造。
