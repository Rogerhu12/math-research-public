# 实际成功输入的通用连续后端

2026-11-10，numerical_recovery。根§13下直接复用数学producer，不再以旧
M15启动/退出包装、冻结、独跑或大型M12参照包为前置。

入口为 `scripts/78718-closed-mode-backend.py`，有三个子命令：`plan`、
`run-stage`、`summarize`。它不修改正在运行的M15。

## 1. 使用方法

以下用未来真正成功的M22 CP举路径例；文件产生前不会编造计划或SHA。
也可以给实际成功的M15、后续M/W分离CP。先在repo根运行：

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
 topics/visible-flexible-closed-surface/scripts/78718-closed-mode-backend.py plan \
 --checkpoint topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m22-direct-01.json.gz \
 --run-directory topics/visible-flexible-closed-surface/notes/2026-11-10-78718-closed-m22-direct-01 \
 --out topics/visible-flexible-closed-surface/notes/2026-11-10-78718-closed-m22-direct-01-plan.json
```

`plan`只读实际CP和它自己最后的完整真尾包。要求原physical RMS、BC、真
outer及实际Jac/audit；不接受UNSOLVED初猜。前缀M与尾W分别读出，不要求相等。
较宽尾的真实完整包始终供export/common-cut使用；不能把高模坡度、二jet或
两个均值丢掉。CP若存低模view，字段必须与同一完整包的明确投影相等。

默认采用已经实际用过的**无损NPZ字节分片**容器；这只改变存储，不改变
数学系数。无需为新的高M故意再制造一次已知的单文件超限。
若需要原单容器，可选 `--container single`，仍保持物理文件4,999,999字节上限。
Cartesian prefix默认 `max(24,M)`；可显式给 `--cartesian-modes` 加密表示。
tail exporter角数取 `max(512,实际尾quadrature)`，所以W22/N1024不会退回N512。
其余深度、临界径向网格、连续区间公式、exact bridge和common-cut算法复用
已执行的原生产链。提高频率没有改变g或相位范围。

计划列41条结构化argv，各分支独立。执行一项：

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
 topics/visible-flexible-closed-surface/scripts/78718-closed-mode-backend.py run-stage \
 --plan topics/visible-flexible-closed-surface/notes/2026-11-10-78718-closed-m22-direct-01-plan.json \
 --stage prefix-base
```

然后 `prefix-target`，可先用 `prefix-inlet-lower` 排除保入口扩张。
这个必要条件只看两轴；未排除不代表整个入口或全图通过。
`prefix-base-metric` 后继续tail-export/radial/collar/first、bridge/common-cut，
再做自己的prefix geometry/metric/moment、background transfer和全tail连续证书。
完整baseline足够就不再算angular；full tail足够就不再算metric-only。
若出现严格点下界超标，应修真正的曲线/尾，不重复该图整套后端。

`run-stage`按原argv执行一项，将stdout/stderr留在该目录的简短运行日志，
保存真实子进程returncode、时间、改变文件的路径/大小/SHA。日志不是工具
会话自然退出的替代，也不把producer exit0等同全图成功。一次只调一个较重
producer；调用者结合当前MemAvailable和活动BVP安排。已有尝试不覆盖。

## 2. 连续数学指标与既有参照

四条最终组合仍是 baseline/angular × full/metric-only。原whole程序保留
同一common map、完整tail与collar覆盖、连续metric/曲率、支撑、moment、
reach和全时相位的计算。其后原terminal巨大参照包装改成小的`summarize`：

- 绑定新whole→自己的closed budget/common map→自己的CP与完整末尾；
- 核真正的mirror/common-cut C²定义和相同g；
- 用准确Fraction核 $U=\max(U_{prefix},U_{tail},0)\le1/500000000$；
- 核 reach/D≥.03、held-region直径/D≥.2、held位移/D≥.05、含反射的
  moment非平凡性及R17材料角作用的全部t；
- 直接引用已有M12点下界证明，不取26+1个旧大参照件。

准确旧下界是
$$L_{12}=\frac{370012576184137}{18889465931478580854784}>1.95883\,10^{-8}.$$
所以新图的完整 $U\le2\,10^{-9}$ 严格推出
$E_{12}>9.79415\,U\ge9.79415\,E_{new}$。
已有R21/R25和本地 `2026-11-09-db6f-root-tail-m12-point-lower-proof.md`
承担这个参照结论；R81/R83给另外的同g加密比较。无需重算旧机械`reference()`。
新图各项上界仍必须来自它自己的数据，不能复制旧M12几何证书。

该摘要之后照原mesh plan/background heights/build交付若干t网格。
保留可选单mesh PL检查工具，删去强制独立同计划字节重跑。
摘要明确没有单独宣称README完成：网格交付和精确解近似的解释由实际数学
结果一并整理，任何旧状态里的“pending independent review”按根§13不再设门。

## 3. 实际已执行范围

工具 **6340d0自然exit0** 以真正成功但已被R81否决原metric门的M14 root02 CP
生成了一个**只含未来命令**的通用计划：41命令、0 producer、0 solver，
所有直接命名的固定背景文件都当前存在。报告为
`2026-11-10-78718-numerical-generic-backend-plan-check.json`，92,403字节，SHA
`71bcf5e1e4e0de3ac11cf7d141febc05c14bba94d356e6f663561476b16af758`。
该实际旧CP只是接口用例，不因计划生成而变成合格图。

工具 **996f79自然exit2** 对旧M15 matched-cut UNSOLVED warm的同一plan请求
明确拒绝“Checkpoint is not an actual successful prefix solve”，未生成生产命令。
此次没有新正向whole报告，也没有假造M15/M22成功结果。
