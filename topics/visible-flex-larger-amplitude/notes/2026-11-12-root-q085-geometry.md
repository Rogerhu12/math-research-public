# 恢复q085的几何筛查与连续reach工具

2026-11-12，visible-larger-20261112。**数值样本与条件证明分开；当前仍为有边前缀。**

运行恢复的first675/loop7.5/sync2、q=.085、M20保存曲线，用其实际物理五次PPoly和完整高度均值。`geometric-neck-prefix-screen.py`现加入每一PPoly段的$(3\pm\sqrt3)/6$内部点；没有把PDE二阶替换为实际曲线导数。命令：

```bash
python computations/geometric-neck-prefix-screen.py \
 --input notes/2026-11-12-strong-first675-q085-m20.json.gz \
 --source-topic /workspace/scratch/c0de65fac774/visible-flex-source/topics/visible-flexible-closed-surface \
 --port computations/alternative-neck-provider-smallcut30-port32-r2048.json \
 --out notes/2026-11-12-root-q085-geometry.json \
 --angular 256 --height-angular 256 --radial 401 --phase-radial 201 \
 --phases 8 --pair-radial 121 --pair-angular 64 --equivalent-default-angle-hook
```

最后一个选项只允许已知的默认cubic兼容扩展：剥去明确的angle hook后，原provider源码SHA256必须与checkpoint完全相同；helper SHA256也固定，profile不得为angle。默认分支仍调用原算术，旧段/knots/jets/height的对照已保存；任意其他源码变化仍拒绝。输出记录该等价理由及全部hash。

## 样本结果

- 3984径向点、每圈256角点：圆柱角绕数为1，角导数和投影Jacobian均为正样本，固定圆柱角的高度没有非正步；最小轴向导数约.07152074。
- 双镜像有边环带的直径云值3.9407783178；最大曲率经局部优化8.3779386853，发生在first descending turn。其样本局部比值$1/(\kappa D)=.0302887128$，只比目标.03略宽。
- 相位点云最大Hausdorff值.1700920，云比值.0431620。点云最近邻离散可能高估连续距离，不能把这个值当连续下界；核心支撑相位差约.16947也仍需排除整面遮挡。
- 18112目标点、2080源查询，在空间半径.2364467内检查319476非零点对，没有法向弦商低于目标.11822335的样本。最小商.12346579；产品分离至少.25时最小.13018223，涉及不相邻loop片时约.13997164。

这些数据表明在**此云**中，局部曲率预算比非局部折回筛查更紧；不提供连续空间结论。未检查点不能因计数为零而消失，环带边界也没有加入帽或处理边界法锥。当前幅度仍远低.2D。

## 连续空间接口

[R16](../results/R16-local-geodesic-and-continuous-reach-cover.md)给出完整证明：若全曲率界为K，内蕴距离≤π/(2K)的点对精确满足两端法向弦界，不额外损失K预算。实际闭图只需对真正非局部且空间距离<2τ的点对支付连续块包络；R11仍准确消除相位变量。

`root_reach_patch_bounds.py`用精确有理数/向上平方根计算块余量，但没有自动认证任何候选的输入半径。当前q085只有样本κ和开放前缀，不能据R16改写成reach证书。后续新g应使用相同筛查定位预算，再对达到幅度的完整候选做真实包络。
