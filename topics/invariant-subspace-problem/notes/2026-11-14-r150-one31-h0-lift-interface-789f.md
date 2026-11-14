# R150：原 h0 的一个 31 分母来源——四阶段执行接口

日期：2026-11-14。本入口的目标是原 $31h_0T$ 模 29791，不是 $H_0=(s-2)h_0$。它继续已完成的[完整315常数组合](2026-11-14-r150-original-h0-one31-denominator-and-seven-rational-directions-789f.md)，未重新生成旧198、旧四列、原首余、已成 selected 来源或图。

**冻结状态：源码和确定的目标模型已准备；执行环境失联后尚未做本入口的 Python 语法检查、原生编译或数学运行。** 这三类状态在 manifest 中保持 false。Actions 首次执行必须取得其真实编译结果；只有最后原17乘回成功才是新的数值证书。

## 1. 唯一原目标及无损输入

整数 primitive 模型仍是原17式、6188个原来源、4367个输出分量。新的模型文本仅改变：

1. magic 改为 R150_ORIGINAL_PH0_MOD29791_V1；
2. 原来的26个 $H_0$ 目标系数，改为 $31h_0$ 的25个系数和末尾补零。

其余4433个原方程系数及18个固定分母/行content系数逐 token 保持不变。生成时还精确检查旧 $H_0=(s-2)h_0$。新 original header 核对全部26个固定目标系数，不只核最高项；旧 $H_0$ 文件不能通过新的 guard。

运行前再将新模型的全部4433原系数及18行缩放模961，与原首余使用的旧整数模型逐项比较，并把新目标除31后与同一旧 $h_0$ 模961比较。由此避免把不同整数方程或不同首余代表混接。

真正的 $x_0$ 来自已保存 initial-standard-source.bin.gz。输入原文件未压缩 SHA256 为 265b0b420afd925d72eb1ab2e2e329fe6232644d740a78aede67866da3545c96。它使用 R150P031、6188原行、九目标、费用85、标准数字0至30。runner 只将它无损改写为 R150PS31 的两字节系数；逐行验证原编号、原方程、364个乘子、权重、全部多项式、最大费用85及1855617个非零系数。没有重新取整或更改 $x_0$。

## 2. 全315常数身份直接内置，未保存的新gzip不成为执行阻碍

已核七列依次为：

$$
(\beta_{199},\beta_{200},\delta_{200},\delta_{201},\delta_{202},\delta_\ell,\delta_{\mathrm{new},j=2}).
$$

runner 保存已核的 $7\times9$ 常数表，并从以下已发布的实际数据逐坐标验证 $\rho_1=\mathcal U C$：

- 原h0首余的完整315系统；
- 旧四个真实第二像列的完整315系统；
- 已恢复新九列的完整global315系统。

第一像的两列还与旧1152列系统的最后两列直接比较，固定其原K199、K200来源。这样不依赖失联环境中尚未上传的新831B证书，也不需要重新运行任何旧数学。

原首余的 NF/Q/余量/trace 从旧落库gzip无损解压并核精确SHA。其余四列、新九列、第一像的数据直接复用 all198 recovery。

## 3. 四个阶段及同一预算

精确入口：

    PYTHONDONTWRITEBYTECODE=1 python \
      2026-11-14-r150-one31-h0-lift-runner-789f.py \
      --notes-root NOTES \
      --t96-recovery T96_RECOVERY \
      --all198-recovery ALL198_RECOVERY \
      --out OUTPUT \
      --math-seconds 120 \
      --memory-mib 512 \
      --compile-seconds 30

可加 --prepare-only，仅完成无损解码、输入核对、完整315常数身份及四编译；可加 --resume-recovery PREVIOUS_OUTPUT/recovery 复用完成缓存和真实数组。T96及all198目录定义与已执行的去P入口相同，只有31个精确输入和8个源码依赖，均由新 contract 锁定。

输入恢复和每个最多30秒的编译在数学计时前；所有四个新阶段共用一个120秒数学 deadline，每个子进程只获得真正剩余时间。每进程512MiB；SIGTERM后最多10秒保存实际数组。无损压缩与manifest生成另计。

1. image：混合原首余、旧四δ、新j2 δ和两β的已存 NF/Q，完整核 $GQ+\mathrm{rem}=\eta$，要求全余为零。
2. source9：同一原完整图计算最终 $VQ$，真kernel标准化，核全部2195来源身份。真实数组和下一图行周期保存，并支持SIGTERM恢复。
3. transport：完整H trace、3333原预基和forward/backward DAG运输到6188原行。这个旧程序没有内部检查点；完成后有内容绑定缓存。
4. original：组成
   $Z=31x_0+31\widehat K F+K_2G+961z$，完整乘回原17式、原6188行、全部4367分量和九目标；原乘积数组、已完成原行和两个源前缀有真正SIGTERM检查点。

image/source9/transport三个C++程序逐字复用已执行版本。original C++只换到独立的固定31h0目标header；它的所有卷积、原行缩放、失败判据与真实checkpoint结构保持不变。

## 4. 费用与准确成功状态

实际原右端费用为87，图给临时来源费用上界183。最终使用实际 transport 费用，并拒绝超出183。不能在运行前宣称新 $Z$ 的实际费用已经是87。

主回执：

    OUTPUT/results/one31-h0-second-lift-pipeline-receipt.json

唯一数值成功要求：

    status == "completed"
    outcome == "one31-denominator-h0-full-original-mod29791-certificate"
    fullOriginalTarget31h0Mod29791IdentityVerified == true
    fullOriginalMod29791IdentityVerified == true
    finite_budget_verified == true

最后原乘积元数据还必须同时核原十七式身份、全部Macaulay身份、行缩放单位及全部费用。零退出码或只有全315相容都不作为最终成功。

成功后的 $Z/31$ 给原固定 $h_0$ 的模 $31^2$ 有理来源近似。旧完整第一障碍说明每个目标在该精度下都必须有31分母。这个事实不证明特征零精确来源已有；后继必须从新的真实 $Z$ 计算余量或做完整来源空间的31饱和，不把固定新代表的下一位失败扩大到全部有理来源。

## 5. 保存与失败

OUTPUT/recovery 保存实际阶段数据、recipe、完成缓存、partial数组和来源前缀。OUTPUT/results 保存回执、日志、全315系数身份、原元数据和全部生成二进制的无损gzip。超过4500000字节则分片，保原SHA、整体压缩SHA和每片SHA。

初始x0无损转换的输出也属于恢复文件；原始大输入可以按其已发布SHA引用，不重复生成。任何超时、外部kill、数学余非零或不完整输出均返回 failed-or-incomplete，并保真实状态。不得把本条冻结源码当作已执行的31h0原式证书。
