# main 普通 ref 竞争的实际恢复（2026-11-12）

run 43303094938 / sync job 131479155073 正式 failure；该轮 interval 和 tail 未开始。实际日志已有两次 non-fast-forward 拒绝，各已马上 git pull --rebase；第三次服务端比较并交换失败报告 cannot lock ref refs/heads/main、is at 与 expected 不同。原发布器未识别这一种并发竞争，抛普通发布错误。随后 finally 保全再次实际 pull 并正常写入源码/失败状态；当前main逐文件已确认request blob13c2280bc513be550441f60416c5cf822c9e8682、runner blob72494c705bf7d03180e054cc4624c655198c9d9a。

修复只在错误明确同时包含 cannot lock ref、refs/heads/main、but expected 时沿用现有立即 pull --rebase 再普通 push 的重试。其它认证/权限/网络错误仍分别保存，绝不强推。没有改变数学源码、全频/mean/逆/精度/资源设置；fresh interval-only启动，原strong继续。
