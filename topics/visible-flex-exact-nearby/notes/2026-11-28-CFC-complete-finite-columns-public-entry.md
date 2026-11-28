# CFC 原 TC96 完整物理列：实际接入与输入清单

日期：2026-11-28 UTC。责任会话：`visible-exact-astra-b0d5a16-20261128`。

本入口继续原 TC 的完整 residual96，不重选或重算已登记的 TC 试探。
它实际补齐全部96个物理目标列的 finite512 载体、无限维 L2 误差及
同源的原 Theta、mean、phase、height 读出。数学合同见
[CFC proof](../results/R149-supplement-complete-normalized-TC-columns-and-finite-physical-interface.md)。

## 必需的实际前置对象

| 前置组 | 必须完整保存的对象 | 原数学责任 |
|---|---|---|
| SC | 三目标的 state/execution、waist/root96 完整对象、两张完整 signed96 gate | 全 TC 三目标和 P224/58/32、negative receivers、JC/RW 的原准入 |
| DCP | 18目标的 manifest/actual/execution 及全部原输入闭包 | 同一 BFP19 全目标误差、WMT/UACT 原 Theta、完整 alpha/model/IR/AS |
| H96 | 七目标的 manifest/actual/execution 及全部原输入闭包 | 原完整 TC/P96/NP/RHI 的相同源及全 mean/physical-coordinate 项 |
| PWA96 | 七目标的 manifest/actual/execution 及完整小输入 | 同一个 shared rho、全部96 exact centres、joint radii、原负窗四 receiver 和 world 两 receiver |

SC 的 whole root96 必须来自
[同一次原计算被动保存接口](2026-11-28-SC-passive-complete-root96-records.md)。
原 $d_j,z_j,e_j$ 已在其唯一纯函数调用中计算；CFC 直接复制保存后的
$e_j$，不再次计算 root norm，也不需要 $D_j/C_R$ 的保守放大。

写作时可见的 reservation 是 H96 run `46123190757/1`、DCP run
`46124617641/1`；reservation 本身不表示科学成功。只有完整实际
结果及成功执行均通过后，generator 才生成有输入 SHA 的 manifest 和
workflow。未给全四组完整实际位置时，当前 metadata readiness 为
`ready:false`，科学调用数0，不生成一个带假占位数据的工作流。

## 新科学对象与载体范围

全部96列是一次整批自然目标，不把成功的单列切成可重跑目标。固定原
source coordinates 后，数学顺序为：

1. 一次512正频 proposal solve 同时选择96个任意 exact-dyadic trials。
   原完整2048 normalizer 系数与全部512输入先做无 alias 的8192 directed
   FFT 卷积，保存完整2560正频像；正向 B 符号为 plus。
2. 共享全部8192单位圆点的 exact-dyadic 幂中心和 disk radius，保留
   每一模式、每一列以及全部新求值误差。完整 quadrature、analytic
   alias、真实 H/finite G 误差、原 w 的两种全误差产品和真 PDE 密度
   误差共同给每列完整目标误差。全部96平方和给 joint bound。
3. 所有512个 true-a 目标坐标保存；真实无限 tail 以 L2 误差保留，
   不把第513模以上当零。原2240 model、全部2048 alpha、true-b 和
   原 C-energy adjoint 的顺序不变；DCP A 的符号为 minus。
4. 同源全部2560 primitive、8192完整 directed FFT、96正 readout、
   2048异号 head、两条 alias rays和完整无限 tail给原 Theta 全矩阵。
   原完整 WMT/UACT global error仍付给每个真实目标误差。
5. 两条真实存储 mean 的 rank仍是1。AP96 的 phase行和PWA96的
   height/reduced-phase行复制全部 exact centres和joint radii，再与
   第一次 SC的完整 e96及原negative root/strict残差结合做新的PDE补正。
   一个共同rho贯穿整行；原negative四输入和独立world两输入全部保留。

每64个模式保存当前同一96列的完整幂、半径、累加值和误差。每个完整
对象先保存读回才进入norm；失败留下准确模式/列位置及whole receipt
chain。原TC仅恢复一个完整 `7671×193×96` value数组并核原SHA，
在waist代数完成后停止，不恢复旧RW96 rows或两张旧SC矩阵。
原w、alpha、model、IR4096、DCP8192都核各自旧wholeSHA。

## 实际执行入口

源码分别为：

- [整批数学](../scripts/fourfold_codazzi_complete_finite_columns_math.py)
- [必要原载体恢复](../scripts/fourfold_codazzi_complete_finite_columns_carriers.py)
- [实际科学 owner](../scripts/fourfold_codazzi_complete_finite_columns_owner.py)
- [公共 worker](../scripts/fourfold_codazzi_complete_finite_columns_public_worker.py)
- [manifest generator](../scripts/make_complete_finite_columns_manifest.py)

generator 的四个 directory 参数都指向真正完整的对应 `run-...-1`
目录；可选同名 manifest 参数固定实际使用的原清单。默认清单路径是
已有各组约定的文件名。完整前置结果出现后使用：

```sh
python topics/visible-flex-exact-nearby/scripts/make_complete_finite_columns_manifest.py \
  --repo . \
  --sc-directory <complete-SC-run-directory> \
  --dcp-directory <complete-DCP-run-directory> \
  --h96-directory <complete-H96-run-directory> \
  --pwa96-directory <complete-PWA96-run-directory>
```

这只生成和校验 metadata，不启动科学工作。生成的 workflow 沿用
不可变 Python container、Python3.12.14、NumPy2.3.5、flint0.9.0、
Haswell和单线程；必要的原14片方向恢复同时保留原SciPy1.17.0、
SymPy1.14.0和mpmath1.3.0，恢复子进程仍按原recipe取消Haswell。
科学时间18000秒，child timeout18600秒；私有磁盘
限额12GiB，科学和execution每个公共文件各小于99000bytes。

公共worker复用完整已锁SC的input/publication前缀及原pull/rebase循环，
明确跳过原SC的consumed-target和科学执行分支。原SC完整输入恢复后，
DCP/H96/PWA的current文件按各自实际checkout，historical文件按原
commit完整恢复；共享文件必须whole bytes一致。新的marker使用新的
CFC目标身份；不会碰旧SC reservation。每次pull继续核根/topic README，
非快进立即rebase再push。所有数组保持job private，不发artifact或Release。

本次已作的验证只有完整AST编译、两个whole-source恢复prefix编译、
proof链接及metadata readiness。没有导入数值库或执行任一新旧科学目标。
独立交叉核验已逐项检查完整same-sign卷积的support、primitive乘子、
正块投影、单位圆幂误差递推以及forward的实重建、measure和alias因子；
这属于静态数学核验，不是目标成功记录。

## 完整方阵尚需的确切对象

本入口提供原完整 $H_{phys}$ 的96列，以及它们的Theta/mean/phase/height
读出。BFP/DCP的strict particular保持独立输入；其direct-nu normalizer、
外mean/Robin和全参数边界列仍各自存在，不能用这一个particular填充。

完整物理square另外需要同一高逆的有符号 `PH^-1 PKQ`、`PH^-1 PU`、
`PH^-1 Pg`，以及同rhs的`PH^-1 Pf`、完整nonmean chart/world/parameter
列、独立physical mean及几何period行。当前没有把这些缺失载体填零。
UACT的真坐标逆保留为坐标工具；一个100×97观察表和本次十目标都不
授完整square、Schur逆或课题完成。
