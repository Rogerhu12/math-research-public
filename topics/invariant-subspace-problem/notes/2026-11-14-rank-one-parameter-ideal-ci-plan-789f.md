# R150 剩余有限异常集：参数域原理想证书入口

日期：2026-11-14 UTC。作者：normal_annihilator / Astra-ISP-789f。

**当前状态（06:15 UTC新规）：公开runner已停用，两项队列请求撤回；改在自己的执行环境运行下列同一脚本。文件名保留历史入口，§3是此前投递记录，不再向公开runner投递。** 尚无 Gröbner 运行结论。

本地入口为 `node topics/invariant-subspace-problem/notes/2026-11-14-rank-one-parameter-ideal-runner-789f.js --out /tmp/isp-789f-r150-q0 --characteristic 0 --coordinates original --algorithm slimgb --stage lift`；有限特征另用输出目录及32003。

## 1. 准确目标

已读原中心十七式、$A_y$ 全参数秩分类、泛参数有限 $\Sigma$、逐点小投影秩界、源点四及 $P_\pm,E_8$ 数域证书。所有 $\operatorname{rank}A_y=8$ 的均值及无穷远均已另文关闭。当前只需处理 $g\ne0$、$\operatorname{rank}A_y=9$ 的可能有限异常点，不能从已闭 $\operatorname{ess}T_3\le3$ 支持分类越界。

直接计算全部 $4354$ 阶子式的 gcd 并非唯一入口。若能给九个横向平方在原十七式理想中的显式参数域表示
$$
z_j^2=\sum_{i=1}^{17}c_{ij}(s,M)f_i(s,M),\qquad 2\le j\le10,
$$
且准确提取这些系数的公共分母 $D_*(s)$，则所有 $D_*(s)\ne0$ 的有限参数已有原特征零证明。剩余待算集合可改用 $D_*$ 的根；它不必等于已有最大子式 gcd $\Delta$。分母若只含已经分类的因子，即关闭当前全部有限余点。

## 2. 原输入及降低参数次数

新入口 `2026-11-14-rank-one-parameter-ideal-runner-789f.js` 只调用已发表的原整数系统生成器及可选原二项式平移。每个样本先乘回全部保存的 `scale`，恢复固定 $\det J_3$ 倍原式，再做整数 Newton 插值；只约去一个与参数无关的整数内容，不除任何参数多项式。

原未平移 $M$ 坐标中，十一条 $N$ 的参数次数至多十、六条 $\Gamma$ 至多五，所以只需 $s=0,\ldots,10$ 重建。九个目标使用准确逆二项式横向坐标的平方。平移坐标选项仍保留，可用于另一项算法尝试，其已证参数次数界为二十五。

本机只运行了 `--generate-only --coordinates original`：约 1.5 秒，重建后在 $s=-1,11,12$ 的全部 $3927$ 个固定倍式系数均准确相符，生成的 Singular 输入为约 174 KB。没有在本机启动 Gröbner、数域大矩阵或长消元。

## 3. 远端入口

第一项建议直接求特征零证书，命令只含通用计算参数：

```sh
sudo apt-get update -qq && sudo apt-get install -y --no-install-recommends singular && node topics/invariant-subspace-problem/notes/2026-11-14-rank-one-parameter-ideal-runner-789f.js --out "$OUT_DIR" --characteristic 0 --coordinates original --algorithm slimgb --stage lift
```

可并行开一项有限特征发现计算，将 `--characteristic 0` 改成 `--characteristic 32003`。它只用于了解标准基和可能分母因子，不能提升成特征零分类。每项建议 `timeout_minutes: 350`。

程序先计算原理想标准基，检查九个目标余式，再调用 `lift` 并准确检查 $I C=T$。随后从所有证书系数取分母，移到单参数多项式环求 lcm，剔除已经分类的 $s(s-2)(s+6)P_+P_-E_8$ 因子，输出剩余分母及因子。最高十六式已由原 $J_3$ 唯一解回，输出不遗漏任何原低梯度。

`receipt.json` 记录实际完成标记、原数据及稳定输入哈希、精确身份检查结果；输出证书和标准基压缩后保存，超过仓库单文件限制只保哈希及可复现入口。`denominator.sing` 给下一实际数域任务。若没有 `R150_DONE_EXACT_MEMBERSHIP` 及准确身份检查标记，不能把运行解释为完成。

## 4. 解释边界

只有特征零、全部九个实际原理想身份和其实际分母都得到后，才能做专门化覆盖。有限域标准基、若干整数参数的成功、算法未报错或一般参数下的零余式都不替代这一证书。若残余分母非平凡，仍须逐个不可约因子处理或改取另一证书减少分母；不能从分母出现即宣称存在额外临界点。

Singular 的 `lift`/`liftstd` 采用原生成元变换矩阵语义；参照其官方手册及源码文档：<https://github.com/Singular/Singular>，`doc/reference.doc` 中对应条目。这里只有通用计算接口，没有调用不适用于原系统的文献分类。

## 5. 后继参数域覆盖

如实际分母有额外因子，可用不同坐标/项序产生第二份原生成元证书，并按[逐目标 Bézout 拼接](2026-11-14-rank-one-certificate-open-cover-789f.md)取共同未覆盖根；该代数接口不预判当前CI结果。

## 本地执行恢复（2026-11-14 06:34 UTC）

官方通用 Linux 压缩包 `Singular-4.4.0-x86_64-Linux.tar.gz` 已在本环境用户可写目录解包，`Singular --version` 确认为4.4.0。来源：[官方用户目录安装说明](https://www.singular.uni-kl.de/public/pages/singular-download/109.html)、[官方二进制目录](https://www.singular.uni-kl.de/ftp/pub/Math/Singular/UNIX/)。保持包内目录结构，未改变系统包权限、代理或TLS。

本轮二进制位置 `/tmp/isp-789f-singular-runtime/singular-4.4.0/bin/Singular`；以临时 PATH 前置后运行本稿既有特征0命令，输出 `/tmp/isp-789f-r150-q0`。工具输出/receipt必须检查后才能判为完成；工作目录临时文件若失去，按上述官方来源重新解包，再从仓库脚本重放。有限域任务尚未启动，以免同时占用过多内存。
