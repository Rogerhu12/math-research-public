# 间隙 23/25 的真实开发尾弯幅、开平 cuff 高度与完整帽

**数值证据。**

冻结 gap 23/25 的同一真实目标与第 2 个已接受的 5292 位置态。改变 R205 整张开发尾的弯幅 A 和实际平 cuff 高 Z；两顶完整 R219 帽相应刚移。开发盘 Cartesian 度量对 A 准确不变，帽的刚体平移保持帽内度量。b..S 上把新减旧端口的全部 P、V、A 及角一、二导乘右端 Hermite 三个函数加入原位置，左接原全函数两 jets、右接新真实 R205 切圈两 jets。S 以后重算整张开发尾，全 cuff 开平 collar 保留。每一组作为固定候选单独比较相位零，相位族内所有帽逐材料点固定。
对所有 15 组各自做完整 4291840 行、原始两网格成本；held 指活动求解域。预选规则是改变的参数中有限 G10 held≥.64 者取最小原成本（若无才考虑其余）。这些是 15 个真实场的初值扫描，优化接受数均为零。

| A | Z | G10 R² | G10 metric | G10 κ | G10 held |
|---:|---:|---:|---:|---:|---:|
| 0.45 | 0.44 | 1.0498122 | 0.494046037 | 21.3220954 | 0.58348803 |
| 0.45 | 0.51 | 1.22574111 | 0.566422417 | 21.337163 | 0.613453581 |
| 0.45 | 0.52 | 1.41273523 | 0.59634098 | 22.586232 | 0.618100005 |
| 0.68 | 0.44 | 0.43118173 | 0.305049065 | 20.1126757 | 0.593946966 |
| 0.68 | 0.51 | 0.13734647 | 0.288838358 | 19.8865066 | 0.617083069 |
| 0.68 | 0.52 | 0.162216138 | 0.320387717 | 19.7326746 | 0.620805481 |
| 0.8746432018 | 0.44 | 0.605235611 | 0.408764388 | 20.1126757 | 0.621173665 |
| 0.8746432018 | 0.51 | 0.0807365047 | 0.201856293 | 19.8865066 | 0.639060058 |
| 0.8746432018 | 0.52 | 0.0818625018 | 0.202392917 | 19.7326746 | 0.642053386 |
| 1.06 | 0.44 | 2.25555636 | 0.699021716 | 20.1126757 | 0.659438857 |
| 1.06 | 0.51 | 0.245769896 | 0.306470313 | 19.8865066 | 0.673342871 |
| 1.06 | 0.52 | 0.226873698 | 0.286122738 | 19.7326746 | 0.675770403 |
| 1.2 | 0.44 | 5.88383605 | 0.9607284 | 24.0766104 | 0.694121009 |
| 1.2 | 0.51 | 0.953548665 | 0.544914893 | 22.2976578 | 0.705845901 |
| 1.2 | 0.52 | 0.836479363 | 0.489922476 | 22.1055752 | 0.70795237 |

选得 A=.8746432018013935、Z=.52。独立 G11 对照原 Z=.51 是 .2017335744 / 19.70704504 / .6392111071，所选为 .2023424235 / 19.55502796 / .6422178391（metric / κ / held）。尾后的持续位置求解从本输入独立 own0 开始。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-gap092-true-tail-amplitude-height.py" --scripts "$S" --prepared polar-new-gap-092-prepared.json --observer polar-new-gap-092-independent.json --state polar-new-gap-092-fixed-step02-step01-state.json --mode select --amplitudes .45 .68 .8746432018013935 1.06 1.2 --heights .44 .51 .52 --output polar-gap092-full-tail-AZ-select.json
python3 -u "$S/2ecf-polar-gap092-true-tail-amplitude-height.py" --scripts "$S" --prepared polar-new-gap-092-prepared.json --observer polar-new-gap-092-independent.json --state polar-new-gap-092-fixed-step02-step01-state.json --mode observe --selection polar-gap092-full-tail-AZ-select.json --output polar-gap092-full-tail-AZ-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-gap092-true-tail-amplitude-height.py | 1aafed2892f615aa25423931d8b67820e3de8faa355ab7b030bb30ebc62797ba |
| polar-gap092-full-tail-AZ-select.json | 3e4a8426686a95d75141fbb4384ee1327c0a476f07edc0ef9133a625b0a41629 |
| polar-gap092-full-tail-AZ-G11.json | 5b6bd7f917ed8eebd5e275d46fe196840d175a5a1f2958efee3866c54d9c303b |
| polar-gap092-full-tail-AZ-select-exit.json | aa40bbe2873f74515157b3eaec33a5fc2a70309c412e16b0dd8830acc3efe88c |
| polar-gap092-full-tail-AZ-select.log | 2dd90fcf4413ed5e73fe8021058c9524228aab6b246a69fcf6c27afb1ba7972b |
| polar-gap092-full-tail-AZ-G11-exit.json | d57b5c4ae2842606c7cc1558794fc57e22077b1ada924a5b61a18fc097708986 |
| polar-gap092-full-tail-AZ-G11.log | dda6ee262ec49a26deac30ed7c9e568a72342aba91c4d76b69d619b3e88d6139 |
