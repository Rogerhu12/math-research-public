# R812 固定六个 CM 代数情形的公开执行

会话 serre-public-astra-20261115。证明见[原apolar源与低矩](../results/R812-original-apolar-source-and-Gaussian-Frobenius-low-moment.md)。这次实际计算尚未返回；所有结果字段须读取公开运行，不能预填非零。

## 固定输入与范围

固定域为 Q(alpha,sqrt3,i)，alpha^3=4、sqrt3^2=3、i^2=-1；原基(S,F,H,R,J,G)、原Miller归一、Gaussian residue sign=+1/-1及实际tame Frobenius j=0,1,2。脚本按原函数域准确构造两方向平移、检查Heisenberg相位/六阶阶数/归一基，再输出六个FG条目、积分幂基分母与Norm；也输出Uhat分母和detUhat的积分Norm。

没有有限素数扫描、高sigma Taylor窗口、ordinary曲线参数改动或新的规范选择。六case中即使有零，真实完整输出仍是成功计算；只有随后分析才能决定非零/单位结论。原同h primitive/Legendre配对与主一致性不由本任务自动宣告完成。

## 源码绑定与运行

- core：topics/serre-uniformity/scripts/R812_tame_theta_transport.py；10634B；SHA256 e7bac15678e6d0d30a30e54edd41a2d34a053b766da97efa7771278827e87ab2。
- wrapper：topics/serre-uniformity/scripts/R812_public_tame_theta_transport.py；11280B；SHA256 416001cae3e161e612fae849519bb9fa4c23f4de0ee601def69d2b3eab88a1ce。
- proof：topics/serre-uniformity/results/R812-original-apolar-source-and-Gaussian-Frobenius-low-moment.md；18812B；SHA256 b538a3bcd47e2638c22b9758050fe87f66381b24fed649e30521092981aeafe1。
- workflow：.github/workflows/serre-fixed-tame-theta-transport.yml；2556B；SHA256 6c4781ceb7ec9a6b5daeaaa39a56ad24615a908570c30811b61ff1c6e69828a4。

请求绑定core/wrapper/proof/workflow；core在任何Sage import及数学前强制公开仓库Actions环境，不提供本地override。wrapper记录实际source/run/attempt、两个README SHA、源码SHA和Python/Sage版本。

使用官方稳定标签 sagemath/sagemath:10.6。宿主先pull并读取RepoDigest，实际以该完整digest启动；镜像ID、digest、平台与版本入运行receipt。源码只读挂载，Sage stdout由宿主保存，容器执行阶段无网络。固定版本10.6已从[Sage官方镜像说明](https://hub.docker.com/r/sagemath/sagemath)及[版本tag](https://hub.docker.com/r/sagemath/sagemath/tags?name=10.6)核实；[10.6 Dockerfile](https://github.com/sagemath/sage/blob/10.6/docker/Dockerfile)确认/usr/bin/sage入口。

core预算30分钟、job45分钟；精确输出由原core断言，wrapper只核来源/schema/完整六cases及canonical JSON SHA，不再次执行数学。结果、日志、完整manifest及源码回执只留一日活跃artifact；不自动进入Git/Release。Git只保存此记录、证明、脚本、参数及以后实际run/SHA/必要解释。

## 规范来源核对

- [Bunkova arXiv:1701.00848v2](https://arxiv.org/html/1701.00848v2)，式(1)、Corollary3.4；仅使用已证明的heat规范/Hurwitz整性，未使用其尚属猜想的精细整除式。
- [Rodriguez Villegas，On the Taylor Coefficients of Theta Functions of CM Elliptic Curves](https://frvillegas.github.io/pdf/frv-cm-theta.pdf)，式(2.8)、(2.16)；本篇D尺度及Gaussian转换在证明内直接校准。
- [FT原六heat笔记](2026-11-15-sigma-full-heat-tame-trivialization-and-even-source.md)。旧材料中若写“R805/FT”，其FT指本笔记，不能与当前R805两仿射图结果混淆。
