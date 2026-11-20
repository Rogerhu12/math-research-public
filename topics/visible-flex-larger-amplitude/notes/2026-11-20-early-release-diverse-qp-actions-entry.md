# R668早释、实际峰覆盖与完整Actions后继入口

2026-11-20，Astra-larger-resume-24b2ab87-20261120。

## 实际范围

本条完成编程、原结果文字归因与完整运行参数准备，没有新的本地科学执行，也没有把未运行代码写成已有效数值方法。[首完整QP](2026-11-20-fullspace-inequality-first-result.md)仍是256乘积后只接受1/4的da088；[R668](../results/R668-feasible-release-before-face-stationarity.md)是完整精确代数证明，新实际效果留待公开Actions。

## 两个分别处理的实际问题

早释源按单位完整坐标范数的可行内向方向下降率选择，保全部原线性不等式的literal最大可行步长。每8次前进、换面或面内梯度已达阈值时考虑释放，阈值为梯度容差与0.1倍面内梯度范数之较大者。首次科学执行前的静态修订只使新释放方向立即进入原步长检查；没有在同一个advance计数先串行释放其它行。旧v1已执行字节不变，早期未执行v2字节可从R668所记普通历史提交恢复。

选行源另修复实际工作集合覆盖：原protected位置仍强制保留；每个protected位置同一原胞、角差≤0.05的永久历史点中，增加本次实际曲率最大点的最大绝对值分支。其余最强直径伙伴的候选，若同胞/同曲率分支且局部坐标差<0.001、角差<1/(32M)，暂不重复占线性名额。没有把这些点从永久非线性screen删除，也不把相近点的曲率当作相等。若还有名额，再保其他真实直径伙伴。192为本批线性工作行上限，不能据此声称整个非线性可行域已经线性描述。

这些是明确的数值工作集选择参数，不是连续曲率证明。原28条821第三盆近重复、真正低phi拒峰未线性化的事实来自已返回的首报告；全部7个新曲率位置/1个半径位置均以纯位置增量保留，包含原实际拒峰本身。

## 全部源身份

| 文件 | 字节 | SHA256 |
|---|---:|---|
| fullspace_feasible_active_cg_v2.py | 20521 | c131b45649e87be2e7f71088d817edb6402a74a4cb50a6b13018e252217f88f7 |
| fullclosed_point_inequalities_v2.py | 12166 | e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8 |
| launch_full_phi_qp_actions.py | 6275 | 6f021d459c24d5cb5a07853628d6a6a297332d51ad561beab2d09e50e2b34d63 |
| check_feasible_active_cg_v2.py | 3664 | bb7f07dbfbbc116315ecd3f5352aeb513dd247005fa67b8500708ac64d197920 |
| inequality-35f-first-new-locations.json | 1756 | a00a6e5e9753cbccd081bb27cecec1dc7e1367bcbb07095a551dbdcbcd5984ae |

## 新执行入口

所有依赖显式从同一repo展开，不依赖调用cwd。原完整driver保持同一全部7377径向观察/2048完整角行、所有原自由量、p8/epsilon.001/scale.05、R664正残差Hessian及真正半梯度。完整坐标为nu_c24正角H²范数加同范数白化2534粗列，mean-Phi单位下阻尼由本次参数给出，不冒同mu与旧粗范数完全相同。

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python "$repo/topics/visible-flex-larger-amplitude/scripts/resume_20261120/launch_full_phi_qp_actions.py" \
 --repo "$repo" --work "$work" \
 --bundle "$work/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four.npz" \
 --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --manifest "$work/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four-witnesses.json" \
 --outdir "$work/full-phi-inequality-v2-first" \
 --damping ACTUAL_DECLARED_MEAN_PHI_DAMPING --directions 1 --maxiter 256
```

上式ACTUAL_DECLARED_MEAN_PHI_DAMPING须由当次明确请求填写真实正数，不能凭占位命令称已运行。launcher的`--print-command`只打印完整命令；实际科学子进程要求公开Actions。完整默认参数在源中逐项展开：192工作行、block32768、band.025、top16/2、safety.992、reach_ratio.03、15回溯、QP atol1e-12/rtol1e-6、线性可行容差2e-11、独立性阈值2e-12。没有Phase-I声称，必须按本轮全部实际永久位置确认零步可行。

本轮重建的-witnesses清单已含全部旧与新位置，并绑定本轮实际carrier，故可直接传入。若另外使用本条历史7κ增量或旧37552B清单，则须沿完整配方先核准确符号节点与同g定义，再显式重绑carrier；不能删去身份字段或把旧carrier冒作新数组。

## 同一必要小QP检查

新check_feasible_active_cg_v2.py只复用原seed2026112007、32变量/28不等式/85数据行/正阻尼.03的小QP以及SLSQP对照，修正提前释放事件名计数。没有增加近相关fixture，也不将未运行fixture列为启动条件；首版中曾写入但未执行的额外fixture已在发表前移除。新的检查仍未运行。其实际报告将分别给出客观差、literal违背、释放方向符号和全部终态诊断，不把旧v1检查值搬到v2。

```sh
python "$repo/topics/visible-flex-larger-amplitude/scripts/resume_20261120/check_feasible_active_cg_v2.py" \
 --source "$repo/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullspace_feasible_active_cg_v2.py" \
 --out "$work/early-release-QP-check.json"
```

完成此程序准备没有支付新候选、全域reach或连续metric，研究继续。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
