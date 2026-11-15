# 最后完整 Dixon 精度的一次独立重建接口

作者：Astra-ISP-789f / normal_annihilator。AI-assisted，GPT-6 Astra Pro。
日期：2026-11-15。

## 1. 具体缺口与范围

冻结的十八右端原单位求解器只在已存 nextrec 日程触发时调用有理重建。
预算末尾的分支只保存完整位状态并退出，不自动尝试最后精度。

真实首段已完成 $653$ 位，第一次续段已从 $653$ 续到 $1205$ 位，
精度 $34946$ bits，累计 $18$ 次重建尚未产生完整有理解。
这只是有限精度与实际尝试的范围；没有从重建未成推出无有理解。

本接口在后续当前轮完成后读取其最后完整状态，**只多做一次该精度的重建**。
不增加 Dixon 位数，不重算逆，不更改原源码，不更改原检查点。
十八右端完整原单位输入与数学 binding 保持不变：

~~~text
2cd043a0fa006deb45f0811412adcd021fb1c0bee395215b812b3d8ad1c5a2af
~~~

本地环境不可用，以下源码仅冻结，未声称已经本地 AST、编译或执行。
实际首次解析、编译和运行由本库 Actions 记录。

## 2. 源码与依赖

| 文件 | 字节数 | SHA256 | Git blob |
| --- | ---: | --- | --- |
| constant-unit-checkpoint-reconstruct-only-789f.cpp | 6460 | 8d32e180db2113fe4bbaa4963cbc0e4a10635e80c32d09c2d93d94c1fbeabe09 | 5b5a69a4b61b796aa15cc673b2693ad97571c45b |
| constant-unit-checkpoint-reconstruct-only-runner-789f.py | 13412 | a9d26fcf924d15069ab979ef3e129339dcb21e3c7b26d1de5607665a3b71cd21 | 883bdce29c44a893aa92d3126905b20d2ec61b90 |

两者完整文件名前缀均为 `2026-11-15-r150-`。

C++ 适配器包含原冻结文件
`2026-11-15-r150-constant-unit-multiple-rhs-dixon-checkpoint-789f.cpp`：

- $19136$ B；
- SHA256 d592f2086e81be2206adb67c7553de15ce36d49a9d1e62721a47a469d8afece2；
- blob 60d874f2b77932609289cdeaac69392de1ccc997。

唯一预处理改动是把原文件的 main 名称改为另一个符号，随后定义适配器自己的 main。
原 Input、Solver、restore、reconstruct、原单位乘回和二进制协议代码原样使用。
它不调用 digit 或 inverse。

编译使用已经实际安装的系统 libflint-dev/libflint22 3.4.0-1：

~~~sh
g++ -std=c++17 -O2 reconstruct-only.cpp -lflint -lgmp -o reconstruct-only
~~~

Python-flint wheel 的版本不充当系统 C++ 头文件或运行库版本。
适配器实际回执另记 header/runtime FLINT 版本。

## 3. 调用与实际输入

~~~sh
python {scripts}/2026-11-15-r150-constant-unit-checkpoint-reconstruct-only-runner-789f.py \
  --pipeline-out {work}/third-missing-four-constant-unit-pipeline \
  --native-source {scripts}/2026-11-15-r150-constant-unit-multiple-rhs-dixon-checkpoint-789f.cpp \
  --adapter-source {scripts}/2026-11-15-r150-constant-unit-checkpoint-reconstruct-only-789f.cpp \
  --out {work}/constant-unit-final-checkpoint-reconstruction \
  --seconds 180 --memory-mib 4096 --compile-seconds 30 \
  --adopt-verified
~~~

最后的 adopt-verified 是明确的可选桥接参数；省略时所有输出只留独立目录。
应在当前原生续轮停止后串行运行本步，不与该续轮同时操作其原目录。

读取的原单位输入为：

~~~text
{pipeline-out}/native-input/actual-constant-unit-eighteen.bin
~~~

其完整字节身份严格为 $9919512$ B，SHA256：

~~~text
02a794f50fcc91e018ec93c941d5974619219edc6bd1225df292907950e33f49
~~~

最后完整状态由原目录 native/checkpoint-active.txt 指向。
runner 读取其真实 slot、digits、prime、bytes、SHA，要求与原生实际回执一致，
再把这些值作为适配器的明确参数。没有把 $1205$ 写成所有未来续轮的硬编码位数。

原位状态可包含较晚的任何完整位数。每次不同的原 active 身份产生不同的
adapter binding；复用同一 out 时只接受同一检查点。若要尝试新的更高精度，
使用新的独立 out。

## 4. 不改原状态的恢复与重建

原 Solver 的 restore 只需要记录的素数，重建本身不需要逆矩阵。
适配器执行：

1. 读取并锁定原 active 元数据与原输入 SHA；
2. 构造原 Solver，令其 p 等于 active 中的真实素数；
3. 调用原 restore，核全部 $X,N$ 字节与 SHA、完整 $p^k$、维数、binding、
   canonical source residues；
4. 把 Solver 的输出目录改为独立的 native-attempt；
5. 调用一次原 reconstruct，不执行任何新 digit；
6. 核位数未变，尝试数只增加一次，原 active 元数据未变。

原 reconstruct 在实际有理恢复前先保存完整尝试检查点，但该文件现在只写入
独立目录。原 slot、原 attempts、原 nextrec 和原 active 指针均不变。
runner 在运行后还重新 SHA 核对原完整 source/residual 文件、原 active 文件和
原生回执，才报告原状态未变。

若有理候选产生，仍须原方法完成全部

$$
4318\times18=77724
$$

个原单位产品，精确验证 $\operatorname{diag}(g)A'\mathrm{Num}=D E$，
才保存同协议 R15CUSL1 的完整 solution。单纯有理重建返回候选不算成功。

无候选或候选不满足全单位身份时，只报告
no-verified-unit-solution-at-this-checkpoint。
预算结束则报告 checkpoint-reconstruction-unfinished。
两者均不作有理解不存在或矩阵秩的新判断。

## 5. 与冻结 final 消费者的显式桥接

若指定 adopt-verified 且完整原单位验证成功，runner：

- 核 solution 全部字节、SHA、binding、维数、素数和位数；
- 保存独立的 unit-solution-adoption-receipt.json，记录原 checkpoint、
  adapter 来源、原冻结 native 来源以及这次实际重建回执；
- 原子复制已验证 solution 到原 pipeline 的 native 目录；
- 写入带该显式 provenance 的 completed native receipt；
- 再核原 active 指针未变。

该步骤只追加真正完成的单位解，不改变原位状态。数学 binding 沿用同一原输入，
新操作的源码、运行和原检查点另有 adapter binding 与 adoption 审计。
它不会把本次独立尝试冒充先前续轮已经执行的重建。

之后继续运行原冻结 pipeline 的 `--through final` 即可。
原消费者会验证 completed solution 的身份并直接跳过原生位循环，
随后执行既定的全部 $4354$ 行残差、缺失两条二阶来源、四条三阶来源及完整第四配对。
本接口不提前宣布这些后继已完成。

若原 pipeline 已有完整单位解，本入口明确停止并要求直接消费该解；
不会再升位或进行不必要重建。

## 6. 预算、输出和准确完成字段

默认数学预算 $180$ 秒、地址空间 $4096$ MiB，编译单独最多 $30$ 秒。
原生 rational reconstruction 若尚在不可中断的 FLINT 调用中，外层在预算后先发
SIGTERM，短暂等待后终止；原检查点不受影响，新尝试的完整前置检查点仍留临时目录。

长期只保存小文本源码、参数、运行身份和：

`constant-unit-last-checkpoint-reconstruction-receipt.json`。

真正单位成功时：

- status=completed；
- outcome=verified-original-unit-solution；
- allOriginalUnitRowsVerified=true；
- originalUnitProductCoordinates=77724；
- newDixonDigitsComputed=0；
- newInverseComputed=false；
- originalActiveManifestUnchanged=true；
- originalCompleteCheckpointUnchanged=true。

即使单位成功，fullOriginal4354VerificationComplete 仍为 false。
只有随后冻结的全原消费者实际乘回，才可提升这一标志。

所有二进制状态、候选和解仅为当前 job 临时数据，不进入 Git、Release 或长期工件。
