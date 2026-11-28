# 同一原始固定 g 的 G10 完整第5—6真步

## 本条消费的原问题

从前条第4真实态接续，采用同一 `2ecf-polar-c2-g10-solve.py`、同一 G10s prepared、独立冻结原 g、原位置源、87×147=12789 个物理 Cartesian 系数和全部 4291840 残差行。958 径点×(128+192) 角均作为训练，所有原13行、q=2面积行、点权、物理 H2 和接受规则保持。没有引入设计 alpha，以下都是这一原固定 g epoch 的实际新接受。

每一步真实重构完整物理 normal，再由原全 J/JT 检查 normal 残差，之后真正评价全非线性目标。本条仅登记已经自然返回的两个步骤。

| 态 | 接受长度 | R14² | metric峰 | 自身κ峰 | min σ | min held | 原normal相对残差 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5 | 1 | 0.14812536874965 | 0.4490434123483 | 198.29478381929 | 0.78299459177121 | 0.71109246622449 | 2.4748402366508e-14 |
| 6 | 1 | 0.11532801883184 | 0.33569347710597 | 132.47542232331 | 0.88504660835771 | 0.71474283067636 | 1.1025010454673e-14 |

两步均在首个完整长度1试值真实接受，没有隐藏被拒长度。第5步λ=2.2222222222222223e−5，因实际/预测下降比小于.25，下一λ加倍；第6步λ=4.4444444444444447e−5，下一λ保持。第6末态累计 own 6次尝试/6次接受，旧4次仅继承，两个新接受独立记账。

| 态 | 自然exit | 实际外部秒 | peak child RSS KiB | G11 metric | G11 自身κ | G11 σ | G11 held |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5 | 0 | 327.683935948 | 555880 | 0.44681404981587 | 197.42530393408 | 0.78170514923865 | 0.71123327902398 |
| 6 | 0 | 357.243779927 | 585620 | 0.33104594131402 | 131.05215495512 | 0.88558285784618 | 0.71487281574707 |

独立 G11 使用668径点、256半步错移角，540径点不在当前 G10 训练中；它只观察同一保存场，不参与本次优化。其所有进程也自然exit0。以上数值是有限训练/独立观察，不是连续曲率、连续浸入或 reach 证书。度量峰与 κ 仍远未到完成要求，不能以正 held 样本替代全闭曲面排球或全时几何。

## 完整接续命令

`S` 为公开课题 scripts；`W` 为含已按前条配方生成 prepared/source、G11源与第4态的工作目录。下列两个步骤精确限定本条新工作；每个真实科学进程由公开 wrapper 留自然退出、墙时和RSS回执，已存在的输出必须使用新目录或前缀。

```bash
for n in 05 06; do
  if [ "$n" = 05 ]; then parent=04; else parent=05; fi
  python3 "$W/2ecf-polar-natural-process-receipt.py" --prefix "$W/polar-G10s-step$n" -- \
    python3 -u "$W/2ecf-polar-c2-g10-solve.py" --scripts "$S" \
    --prepare-entry "$W/2ecf-polar-c2-g10-split-prepare.py" \
    --prepared "$W/polar-c2-G10s-prepared.json" \
    --state "$W/polar-G10s-step$parent-step01-state.json" --prefix "$W/polar-G10s-step$n" --steps 1
  python3 "$W/2ecf-polar-natural-process-receipt.py" --prefix "$W/polar-G11r-G10s-step$n" -- \
    python3 -u "$W/2ecf-polar-c2-independent-g11-resume-observe.py" observe --scripts "$S" \
    --prepare-entry "$W/2ecf-polar-c2-g10-split-prepare.py" \
    --prepared "$W/polar-c2-G10s-prepared.json" \
    --observer "$W/polar-independent-G11r-shifted256-independent.json" \
    --state "$W/polar-G10s-step$n-step01-state.json" --output "$W/polar-G11r-G10s-step$n.json"
done
```

当前输入同一 G10s prepared 的 SHA 为 `de75e9632855bc3547e174d7e1bfcefaa295d01dbe151d1c087ff0d83682df80`；入口 SHA 为 `baad827f707e889f1be395d7b010dc91c1f39ce21bebdd5042e992038ffce642`。原完整重生配方在 G10 complete-source/four-baselines 记录；这里没有把临时绝对路径当作唯一恢复入口。

| 文件 | SHA256 |
|---|---|
| `polar-G10s-step05-step01-state.json` | `b3b165fa9a9b70fa51bf27bdac3541ce53b0de0249a9f37854a01207efa56b3b` |
| `polar-G10s-step05-exit.json` | `914f9a395e0ec4fcf8fbcd50e353537ed02ce57784d3b7f9fa35617128202e91` |
| `polar-G11r-G10s-step05.json` | `bdf19f52026e27f35f73c476786b885356a1b14aef764f20ab689577e8fbb9ee` |
| `polar-G11r-G10s-step05-exit.json` | `292916fbaf536b0af4d519467839e7f693ea256ed66060094baee2516d8ebf49` |
| `polar-G10s-step06-step01-state.json` | `5cd09c6742eb5b7ae7bc3e3a291aae5d2483f8c7d7ad3adfe93af1a3e1649440` |
| `polar-G10s-step06-exit.json` | `f7eb9f0208e38da4adb2e582d4688a6f69219c77b5a88992356379689e1b0b26` |
| `polar-G11r-G10s-step06.json` | `92e17e5ee4c1818d638a5b30cd9ca0dc536ba788b8e4f1cca0faf86a661095e2` |
| `polar-G11r-G10s-step06-exit.json` | `cef452b7d3a1a07179392c4538d782c804eefc9e17ac20ec931a014503a145d1` |
